from django.conf import settings
from django.db import models

# Create your models here.

class Quartos(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Título')
    description = models.TextField(max_length=200, verbose_name = 'Descrição')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Preço')
    peoples = models.DecimalField(max_digits=2, decimal_places=0, verbose_name = 'Capacidade de pessoas')
    smoke = models.BooleanField(default=True, verbose_name = 'Permitido Fumar')
    # image = models.ImageField(
    #     upload_to = 'static/images/',
    #     null = True, blank = True,
    #     verbose_name = 'Imagem do quarto')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Quarto'
            verbose_name_plural = 'Quartos'
