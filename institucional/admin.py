from django.contrib import admin
from .models import Home
from .models import Quemsomos
from .models import Contato

# Register your models here.

admin.site.register(Home)
admin.site.register(Quemsomos)
admin.site.register(Contato)
