from django.db import models

# Create your models here.


class Moeda(models.Model):
    pais = models.CharField(max_length=50)
    pais_codigo = models.SmallIntegerField()
    sigla_swift = models.CharField(max_length=3)
