from django.db import models
from ..users.models import UserModel
class ShopingHistoryModel(models.Model):
    fechaCompra = models.DateField(auto_now_add=True, db_column='fecha_compra')
    totalGastado = models.FloatField(null=False)
    id_usuario = models.ForeignKey(
        to=UserModel, on_delete=models.PROTECT, db_column='id_usuario', related_name='historial_compras')
    
    class Meta:
        db_table='historial_compras'