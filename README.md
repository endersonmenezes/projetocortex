# 1 - Projeto Cortex

Este projeto desenvolve uma API REST utilizando o Django. O seu código segue o padrão do Django com a Documentação do Django Rest Framework.

Bibliotecas:
- [Django](https://docs.djangoproject.com/en/3.1/)
   - [Cache Framework](https://docs.djangoproject.com/en/3.1/topics/cache/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
- [Django Decouple](https://github.com/henriquebastos/python-decouple)
- [Django Celery Results](https://pypi.org/project/django-celery-results/)
- [Gunicorn](https://gunicorn.org/#docs)
- [Requests](https://requests.readthedocs.io/en/master/)

OBS1: Os commits contem um histórico do código.

OBS2: Vou tentar desenvolver o sistema de Fila e Cache.

## 1.0 - Projeto

A rota está disponível na raiz.

Ex: **/?moeda_origem=BRL&moeda_destino=USD&valor_desejado=10&data_cotacao=10/09/2019**

A rota **/admin/** vai conter um administrador das moedas cadastradas.

Para acessar o admin é necessário criar um usuário com o comando:
````shell
# Dentro do container dj
python manage.py createsuper user

# Dentro no heroku
heroku run python manage.py createsuperuser -a <nome_do_projeto>
````


## 1.1 - O desafio

Neste projeto o meu intuito é disponibilizar uma API REST que consulte a cotação do Banco do Brasil. 
A API recebe **data_cotacao**, **moeda_origem**, **moeda_destino**, **valor_desejado**. O retorno é **valor**.

- data_cotacao:  Data para realizar a cotação.
- moeda_origem: Código da moeda origem.
- moeda_final: Código da moeda desejada.
- valor_desejado: Valor desejado de conversão.
- valor: Retorno do valor desejado.

## 1.1 - Comentário

Consegui realizar o estudo da API, utilizando o console de desenvolvedor. Achei todas as pontas da API e desenvolvi a solução desejada.

## 1.2 - O desafio

Estruturar uma arquitetura que seja capaz de utilizar o serviço desenvolvido acima, com um sistema de cache (30 min). 

Estruturar um sistema de Fila para consumo do serviço onde possa existir uma maneira especial de "furar_fila".

[O diagrama está disponível aqui.](/arquitetura-cortex.pdf)

## 1.2 - Comentário

Nunca utilizei uma documentação como aprendi na faculdade UML e etc, acho que com mais convicio com isso com certeza iria pegar mais o jeito, a documentação ficou simples, porém de bonus, ativei o sistema de cache, não desenvolvi a fila, por que meu contato com RabbitMQ foi mais pra robotização, apesar de saber que o apply() de uma função pode ir para uma fila especifica. O sistema do Cache do Django também foi algo novo, porém simples, vi que na documentação tem como ativar keys para quando for algo do cache, porém não consegui usar.

# 2 - Development

Para teste e desenvolvimento iremos utilizar o Docker para criar as máquinas. Clone o repositório e siga os passos abaixo.

````bash
# É necessário instalar o Docker em seu computador, e executar dois comandos.

# Monte os containers que iremos utilizar
docker-compose build

# Suba os containers
docker-compose up

# Rode as migrations do Banco de Dados
docker-compose run dj python manage.py migrate

# Execute uma tarefa manual de coletar as moedas
docker-compose run dj python manage.py shell
>> from modulo_bc.tasks import get_moedas_bc
>> get_moedas_bc.apply()
# Pressione Ctrl + D para sair.
````

# 3 - Production

A build de produção desse projeto estará disponivel no Heroku, [clicando aqui](https://projetocortex.herokuapp.com/). E os passos abaixo podem ser seguidos para criar o seu próprio app. 

## 3.1 - Arquivos Necessários

O Heroku necessita para identificar que é uma aplicação em Python, do **runtime.txt**, e para identificar que é uma aplicação o **Procfile** identificando o WSGI do Cortex como principal.

- Instale o CLI do Heroku para o seu SO. [Clique aqui](https://devcenter.heroku.com/articles/heroku-cli).
- Crie uma aplicação e selecione o deploy dela como o seu repositório Fork deste no Github.

```bash
# Instale o sistema de gerenciamento de configurações.
heroku plugins:install heroku-config

# Envie as configurações locais do .env para seu projeto
heroku config:push -a <nome_do_projeto>

# Realize as migrações necessárias. Esse procedimento é necessário sempre que um deploy conter uma migração.
heroku run python manage.py migrate -a <nome_do_projeto>

# Baixe as moedas inicialmente
heroku run python manage.py shell
>> from modulo_bc.tasks import get_moedas_bc
>> get_moedas_bc.apply()
```

- Use o CloudAMPQ do Heroku
   - [Clique aqui](https://devcenter.heroku.com/articles/cloudamqp#installing-the-add-on) para acessar a documentação.

- Estamos utilizando um S3 da Amazon para subir os arquivos.
   - [Clique aqui para ter acesso a documentação](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)

# 4 - TODO

- [X] Configuração inicial do Django
- [X] Configuração do Docker
   - [X] Configuração do RabbitMQ
   - [X] Configuração do Celery Service
   - [ ] Verificar gerenciamento de Fila
   - [X] Gerenciamento de Cache do Django
- [X] Verificação da API do Banco Central
- [X] Configuração do RabbitMQ