# Generated by Django 5.0.2 on 2024-02-28 03:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_history', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinghistorymodel',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.PROTECT, related_name='historial_compras', to=settings.AUTH_USER_MODEL),
        ),
    ]
