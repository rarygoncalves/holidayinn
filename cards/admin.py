from django.contrib import admin
from .models import Quemsomos
from .models import Promocoes
from .models import Acomodacoes

# Register your models here.

admin.site.register(Quemsomos)
admin.site.register(Promocoes)
admin.site.register(Acomodacoes)
