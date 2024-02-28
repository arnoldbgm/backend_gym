from django.db import models
from ..shopping_history.models import ShopingHistoryModel
from ..products.models import ProductsModel

class ShoppingDetailModels(models.Model):
    cantidadComprada = models.IntegerField(null=False)
    precioUnitario = models.FloatField()
    id_compra = models.ForeignKey(
        to=ShopingHistoryModel, on_delete=models.PROTECT, db_column='id_usuario', related_name='historial_compras')

    id_producto = models.ForeignKey(
        to=ProductsModel, on_delete=models.PROTECT, db_column='id_producto', related_name='productos')
    class Meta:
        db_table= 'detalles_compra'