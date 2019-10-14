from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def index(request):
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

    return render(request, 'core/index.html')
