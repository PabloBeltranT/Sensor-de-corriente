from django.db import models

# Create your models here.
class Datos_de_consumo(models.Model):

    fecha = models.CharField(max_length=50)
    hora  = models.CharField(max_length=50)
    corrinete_consimuda_en_directa = models.CharField(max_length=50)
    potencia_consumida_en_directa  = models.CharField(max_length=50)
    timepo_de_consumo_en_red_comercial = models.CharField(max_length=50)
