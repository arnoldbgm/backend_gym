from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers.serializers import RegisterProductSerializer
from .models import ProductsModel
# Create your views here.


class CreateProductsView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializador = RegisterProductSerializer(data=request.data)
        print(type(serializador))
        validacion = serializador.is_valid()
        if validacion is False:
            return Response(data=serializador.errors)

        nuevoProducto = ProductsModel(**serializador.validated_data)
        nuevoProducto.save()
        return Response(data={
            'msg': f'El producto fue creado exitosamente {request.data["nombreProducto"]}', 
            'data': serializador.data}, status=201)
