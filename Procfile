web: gunicorn cortex.wsgi
worker: celery -A cortex beat -l info --pidfile=