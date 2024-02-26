from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password, telefono):
        if not correo:
            raise ValueError("El usuario no proporciono el correo")
        correo_normalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(correo=correo_normalizado, nombre=nombre, apellido=apellido,
                                   tipoUsuario=tipoUsuario, telefono=telefono)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()
