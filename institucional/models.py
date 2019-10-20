from django.conf import settings
from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=20, verbose_name = 'Título')
    description = models.TextField(max_length=100, verbose_name = 'Descrição')
    active = models.BooleanField(default=False, verbose_name = 'Selecionar como primeiro slide')
    image = models.ImageField(
        upload_to = '',
        null = True, blank = True,
        verbose_name = 'Imagem do slide')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Slide'
            verbose_name_plural = 'Slides'

class Quemsomos(models.Model):
    title = 'Missão | Visão | Valores'
    description = models.TextField(max_length=200, verbose_name = 'Descrição')
    mission = models.TextField(max_length=300, verbose_name = 'Missão')
    vision = models.TextField(max_length=300, verbose_name = 'Visão')
    value = models.TextField(max_length=300, verbose_name = 'Valores')

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Quem Somos'
            verbose_name_plural = 'Quem Somos'

class Contato(models.Model):
    title = 'Endereço | Telefone | Email'
    address = models.TextField(max_length=100, verbose_name = 'Endereço')
    telephone = models.TextField(max_length=100, verbose_name = 'Telefone')
    email = models.TextField(max_length=100, verbose_name = 'Email')


    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Contato'
            verbose_name_plural = 'Contato'
