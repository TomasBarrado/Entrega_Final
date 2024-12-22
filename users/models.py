from django.db import models
from django.contrib.auth.models import User

class Imagen(models.Model):
    """
    Modelo para manejar las imágenes de perfil de los usuarios.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="avatar")
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True, default='avatares/default.png')

    def __str__(self):
        return f"Avatar de {self.user.username}"

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
