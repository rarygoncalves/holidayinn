from django.conf import settings
from django.db import models

# Create your models here.

class Quartos(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    smoke = models.BooleanField(default=True)
    peoples = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Quarto'
            verbose_name_plural = 'Quartos'
