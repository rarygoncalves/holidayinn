from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from institucional.models import Home
from institucional.models import Quemsomos
from promocoes.models import Promocoes
from acomodacoes.models import Quartos
from institucional.models import Contato

# Create your views here.

def index(request):

    # Configurando formulário
    if request.method == 'POST':
        nome = request.POST['nome']
        cel = request.POST['cel']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject,
        (f'Nome: {nome}\nTelefone: {cel}\nE-mail: {email}\nMensagem: {message}'),
        settings.EMAIL_HOST_USER,
        ['traineeholidayinn@gmail.com'],
        fail_silently=False)

    list_home = Home.objects.all()
    quemsomos = Quemsomos.objects.get(pk=1)
    list_promocoes = Promocoes.objects.all()
    list_quartos = Quartos.objects.all()
    contato = Contato.objects.get(pk=1)

    return render(request, 'index.html', {'list_home': list_home, 'quemsomos': quemsomos, 'list_promocoes': list_promocoes, 'list_quartos': list_quartos, 'contato': contato})
