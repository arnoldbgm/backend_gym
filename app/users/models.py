from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth.auth_models import UserManager

class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
    correo = models.EmailField(max_length=200, unique=True)
    password = models.TextField(max_length=100, null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('CLIENTE', 'CLIENTE')
    ])
    telefono = models.CharField(max_length=12)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario','telefono'] #El orden en que se va a mostrar los datos en la terminal

    objects = UserManager()  # instancia de config

    class Meta:
        db_table = 'usuarios'
