from rest_framework import serializers
from ..models import ProductsModel


class RegisterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'
