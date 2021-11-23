from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class CustomAccountManager(BaseUserManager):
    def create_user(self, correo, nombre, password, **other_fields):
        correo = self.normalize_email(correo)
        if not correo:
            raise ValueError(_('Debes ingresar un correo'))
        user = self.model(correo=correo, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, correo, nombre, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(correo, nombre, password, **other_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    correo =  models.EmailField(verbose_name='Correo', unique=True)
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self) -> str:
        return self.correo

class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(verbose_name='Dirección', max_length=255)


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)