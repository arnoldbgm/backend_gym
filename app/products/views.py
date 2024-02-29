from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers.serializers import RegisterProductSerializer, ObtainAllProductsSerializer, GetOneProductsSerializer
from .models import ProductsModel
# Create your views here.


class CreateProductsView(CreateAPIView):

    # 1ra forma de como escribir el metodo post
    # def post(self, request, *args, **kwargs):
    #     serializador = RegisterProductSerializer(data=request.data)
    #     print(type(serializador))
    #     validacion = serializador.is_valid()
    #     if validacion is False:
    #         return Response(data=serializador.errors)

    #     nuevoProducto = ProductsModel(**serializador.validated_data)
    #     nuevoProducto.save()
    #     return Response(data={
    #         'msg': f'El producto fue creado exitosamente {request.data["nombreProducto"]}',
    #         'data': serializador.data}, status=201)

    serializer_class = RegisterProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={
            'msg': f'El producto fue creado exitosamente {serializer.validated_data["nombreProducto"]}',
            'data': serializer.data
        }, status=201, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class GetAllProductsView(ListAPIView):
    serializer_class = ObtainAllProductsSerializer
    queryset = ProductsModel.objects.all()


class DeleteOneProductView(DestroyAPIView):
    def delete(self, request, pk: int):
        product = ProductsModel.objects.filter(id=pk).first()
        if product is None:
            return Response(data={'msg': 'No se encontró el producto solicitado'}, status=404)

        product.delete()
        return Response(data={'msg': 'El producto se eliminó exitosamente'}, status=204)


class GetSingleProductView(RetrieveAPIView):
    def get(self, request, pk: int):
        product = ProductsModel.objects.filter(id=pk).first()
        if product is None:
            return Response(data={'msg': 'El producto que estas buscando no existe'}, status=404)
        serializador = GetOneProductsSerializer(product)
        return Response(data={'msg': 'El producto se encontro exitosamente', 'data': serializador.data}, status=201)
