# Projeto Cortex

Este projeto desenvolve uma API REST utilizando o Django. O seu código segue o padrão do Django com a Documentação do Django Rest Framework.

Bibliotecas:
- [Django](https://docs.djangoproject.com/en/3.1/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
- [Django Decouple](https://github.com/henriquebastos/python-decouple)
- [Django Celery Results](https://pypi.org/project/django-celery-results/)
- [Gunicorn](https://gunicorn.org/#docs)

# Commits

O histórico de commits foi feito detalhado, cada "bloco" de alterações, a criação de um modulo, a instação de uma biblioteca.

# .gitignore

Arquivos como por exemplo .env estariam no .gitignore, no exemplo eu não coloquei para facilitar o clone e build dev. Nos projetos geralmente eu utilizo o site [gitignore.io](https://www.toptal.com/developers/gitignore) para ver uma base, principalmente quando estou iniciando na linguagem, conforme o projeto vai crescendo acabo tendo o meu "exemplo" a ser copiado.

# Building Development

Para teste e desenvolvimento iremos utilizar o Docker para criar as máquinas.

# Building Production

A build de produção desse projeto estará disponivel no Heroku, [clicando aqui](https://projetocortex.herokuapp.com/). E os passos abaixo podem ser seguidos para criar o seu próprio app. 

## Arquivos Necessários

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
```

# TODO

- [X] Configuração inicial do Django
- [ ] Configuração do Docker
   - [ ] Configuração do RabbitMQ
   - [ ] Configuração do Celery Service
   - [ ] Configuração do Celery Beat
   - [ ] Verificar gerenciamento de Fila
- [ ] Verificação da API do Banco Central
- [ ] Configuração do RabbitMQ