from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('id', 'nombre', 'apellido', 'correo', 'telefono', 'is_staff', 'is_active', 'tipoUsuario')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('correo', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'telefono')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'tipoUsuario')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo', 'nombre', 'apellido', 'telefono', 'password1', 'password2', 'is_staff', 'is_active', 'tipoUsuario')}
        ),
    )
    search_fields = ('correo', 'nombre', 'apellido')
    ordering = ('id',)

admin.site.register(UserModel, CustomUserAdmin)
