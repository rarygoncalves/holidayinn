from django.conf import settings
from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=20, verbose_name = 'Título')
    description = models.TextField(max_length=300, verbose_name = 'Descrição')
    active = models.BooleanField(default=False, verbose_name = 'Selecionar como primeiro slide')
    # image = models.ImageField(
    #     upload_to = 'static/images/',
    #     null = True, blank = True,
    #     verbose_name = 'Imagem do slide')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Slide'
            verbose_name_plural = 'Slides'

class Quemsomos(models.Model):
    title = models.CharField(max_length=20, verbose_name = 'Título')
    description = models.TextField(max_length=300, verbose_name = 'Descrição')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Quem Somos'
            verbose_name_plural = 'Quem Somos'
