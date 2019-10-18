from django.conf import settings
from django.db import models

# Create your models here.

class Promocoes(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Título')
    description = models.TextField(max_length=200, verbose_name = 'Descrição')
    image = models.ImageField(
        upload_to = '',
        null = True, blank = True,
        verbose_name = 'Imagem da Promoção')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Promoção'
            verbose_name_plural = 'Promoções'
