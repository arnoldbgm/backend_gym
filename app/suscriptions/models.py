from django.db import models
from ..users.models import UserModel


class SuscriptionsModel(models.Model):
    tipoSuscripcion = models.CharField(max_length=40, choices=[
        ('FULL', 'FULL'),
        ('INTER', 'INTERDIARIO'),
        ('MAQ', 'SOLO MAQUINAS'),
        ('DANCE', 'SOLO BAILE')
    ])
    precioTotal = models.FloatField(null=False)
    precioPagado = models.FloatField(null=False)
    descuento = models.FloatField(null=False)
    fechaInicio = models.DateField(null=False)
    fechaFin = models.DateField(null=False)
    estado = models.CharField(max_length=40, choices=[
        ('ALDIA', 'AL DIA'),
        ('PENDIENTE', 'PENDIENTE DE PAGO'),
        ('BLOQUEADO', 'BLOQUEADO'),
    ])
    id_usuario = models.ForeignKey(
        to=UserModel, on_delete=models.PROTECT, db_column='id_usuario', related_name='suscripciones')

    class Meta:
        db_table = 'suscripciones'
