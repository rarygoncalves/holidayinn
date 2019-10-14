from django.conf import settings
from django.db import models

# Create your models here.

class Quemsomos(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Quem Somos'
            verbose_name_plural = 'Quem Somos'
