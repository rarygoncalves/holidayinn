<img src="core/static/images/logo.png" alt="Holiday Inn" width="300"/>

# Holiday Inn - Trainee 2019.2 <a href="http://www.ejectufrn.com.br"><img src="http://static.ejectufrn.com.br/eject/blog/img/logo.svg" alt="EJECT" width="120"/></a>

Site desenvolvido para avaliação do Trainee 2019.2 da Empresa Júnior da Escola de Ciências e Tecnologia (EJECT) da Universidade Federal do Rio Grande do Norte (UFRN).

## Time de Desenvolvimento

:bust_in_silhouette: [Alisson Andrade](https://github.com/AlisoSouza)

:bust_in_silhouette: [Gustavo Alessandro](https://github.com/gustavoUfrn/)

:bust_in_silhouette: [João Henrique](https://github.com/joaohsc/)

:bust_in_silhouette: [Rary Gonçalves](https://github.com/rarygoncalves/)

## Tecnologias Utilizadas

#### BACK-END

|Python|Django|
|------|------|

#### FRONT-END

|HTML|CSS|JavaScript|
|----|---|----------|

## Execução do Projeto

Inicialmente, recomenda-se o uso de um ambiente virtual de desenvolvimento Python para execução do projeto em sua máquina local. Como sugestão, deixamos aqui o site do Anaconda, um ambiente virtual baseado em Python:

[Site para download do Anaconda](https://www.anaconda.com/products/individual)

> Configure o seu ambiente com a versão do Python 3.6 ou superior.

Uma vez instalado e configurado seu ambiente virtual de desenvolvimento, você pode realizar um clone do repositório do Holiday Inn para sua máquina local:

`$ git clone https://github.com/rarygoncalves/holidayinn.git`

Assumindo que já está em seu ambiente virtual de desenvolvimento, entre no diretório raiz do projeto onde haverá o arquivo **requirements.txt** com as dependências e bibliotecas utilizadas no projeto e instale-as usando o gerenciador de pacotes Python **pip**:

```
pip install -r requirements.txt
```

Agora você deve criar o banco de dados e realizar as migrações para que o DB esteja pronto para conexão e uso pelo Django:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

> Foi utilizado o SQLite como Banco de Dados desse projeto, que é o banco padrão do Django. Mas há suporte para outros SGDBs como MySQL, PostgreSQL, MariaDB e Oracle (consultar documentação de conexão e integração caso deseje usá-los).

Por fim, você deve criar um superusuário para que tenha acesso ao Django Admin:

```
$ python manage.py createsuperuser
```

Agora você já pode rodar o projeto Django localmente:

```
$ python manage.py runserver
```

Feito isso, assumindo que nenhum erro foi apresentado em seu terminal, você receberá uma saída semelhante à esta:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 16, 2020 - 20:15:42
Django version 2.2, using settings 'holidayinn.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Pronto!
O projeto está rodando em `localhost:8000` ou `127.0.0.1:8000`

> Você pode ter acesso à dashboard de admin pela url `localhost:8000/admin`
