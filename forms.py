from django.conf import forms

# Create your models here.

class Formulario(forms.Form):
    name = forms.CharField(max_length=50)
    cel = forms.CharField(max_length=18)
    email = forms.CharField(max_length=45)
    subject = forms.CharField(max_length=45)
    message = forms.TextField(max_length=1000)

