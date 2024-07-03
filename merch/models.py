from django.db import models 

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    precio = models.FloatField()
    fabricante = models.CharField(max_length=50)

class DVDs(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    precio = models.FloatField()
    tipo = models.BooleanField()
    en_stock = models.BooleanField()


class Distribuidor(models.Model):
    distribuidora = models.CharField(max_length=50)
    repartidor = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    