from django.db import models

# Create your models here.


class Moeda(models.Model):
    pais_nome = models.CharField(max_length=50)
    pais_codigo = models.SmallIntegerField()
    moeda_swift = models.CharField(max_length=3)
    moeda_codigo = models.SmallIntegerField()
