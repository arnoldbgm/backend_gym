from rest_framework import serializers
from ..models import ProductsModel


class RegisterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'


class ObtainAllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'


class GetOneProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'

class PatchProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'
