from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers.serializers import RegisterProductSerializer, ObtainAllProductsSerializer, GetOneProductsSerializer, PatchProductsSerializer
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


class PatchProductsView(UpdateAPIView):
    # serializer_class = PatchProductsSerializer

    def update(self, request, pk=int, **kwargs):
        product = ProductsModel.objects.filter(id=pk).first()
        if not product:
            return Response(data={'msg': 'El producto que estás intentando actualizar no existe'}, status=404)

        serializer = PatchProductsSerializer(
            #instance valor que se actualizara
            #data el valor que enviamos
            #partial señala como se actualizara
            instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_data = serializer.validated_data

        if updated_data.get('nombreProducto') == product.nombreProducto:
            return Response(data={'msg': 'Estás enviando el mismo nombre del producto que está registrado en la base de datos'}, status=400)

        if updated_data.get('precioProducto') == product.precioProducto:
            return Response(data={'msg': 'Estás enviando el mismo precio del producto que está registrado en la base de datos'}, status=400)

        if updated_data.get('cantidadProducto') == product.cantidadProducto:
            return Response(data={'msg': 'Estás enviando la misma cantidad del producto que está registrada en la base de datos'}, status=400)

        serializer.save()
        return Response(data={'msg': 'El producto se actualizó exitosamente', 'data': serializer.data}, status=200)
