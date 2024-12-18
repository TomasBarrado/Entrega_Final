from django.db import models
from django.contrib.auth.models import User


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} (Matrícula: {self.matricula})"
