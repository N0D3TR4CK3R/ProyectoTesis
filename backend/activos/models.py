from django.db import models

# Create your models here.

class Activo(models.Model):
    tipo_activo = models.CharField(max_length=100)
    nombre_activo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_activo} ({self.tipo_activo})"
