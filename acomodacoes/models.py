from django.conf import settings
from django.db import models

# Create your models here.

class Promocoes(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Promoção'
            verbose_name_plural = 'Promoções'

class Acomodacoes(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Acomodação'
            verbose_name_plural = 'Acomodações'
