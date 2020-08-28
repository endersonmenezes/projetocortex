# RabbitMQ
FROM rabbitmq:3-management
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp

FROM python:3
# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN apt update \
    && apt install -y gcc python3-dev curl ca-certificates wget gnupg2 default-libmysqlclient-dev build-essential

# Directory Structure
RUN mkdir -p /backend \
    && mkdir -p /emails \
    && mkdir -p /logs \
    && mkdir -p /media

# Set work directory.
WORKDIR /code

# Copy project code.
COPY ./ /code/

# Install dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "cortex.wsgi:application"]

CMD ["python", "manage.py", "migrate"]