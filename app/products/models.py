from django.db import models


class ProductsModel(models.Model):
    nombreProducto = models.CharField(max_length=100)
    precioProducto = models.FloatField(null=False)
    cantidadProducto = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'productos'