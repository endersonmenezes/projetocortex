# Projeto Cortex

Este projeto desenvolve uma API REST utilizando o Django. O seu código segue o padrão do Django com a Documentação do Django Rest Framework.

Bibliotecas:
- [Django](https://docs.djangoproject.com/en/3.1/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
- [Django Decouple](https://github.com/henriquebastos/python-decouple)
- [Django Celery Results](https://pypi.org/project/django-celery-results/)

# Commits

O histórico de commits foi feito detalhado, cada "bloco" de alterações, a criação de um modulo, a instação de uma biblioteca.

# .gitignore

Arquivos como por exemplo .env estariam no .gitignore, no exemplo eu não coloquei para facilitar o clone e build dev. Nos projetos geralmente eu utilizo o site [gitignore.io](https://www.toptal.com/developers/gitignore) para ver uma base, principalmente quando estou iniciando na linguagem, conforme o projeto vai crescendo acabo tendo o meu "exemplo" a ser copiado.

# Building Development

Para teste e desenvolvimento iremos utilizar o Docker para criar as máquinas.

# Building Production

A build de produção desse projeto estará disponivel no Heroku, [clicando aqui](https://projetocortex.herokuapp.com/). E os passos abaixo podem ser seguidos para criar o seu próprio app. 