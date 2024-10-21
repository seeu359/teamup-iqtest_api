FROM python:3.10-slim AS builder

WORKDIR /opt/app

COPY .. .

RUN  apt-get update && apt-get install -y build-essential python3-dev && \
	python -m venv /opt/app/venv && \
	. /opt/app/venv/bin/activate && \
 	pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY .. .

COPY --from=builder /opt/app/venv /opt/app/venv

WORKDIR /opt/app
EXPOSE 8000

RUN . /opt/app/venv/bin/activate && python manage.py makemigrations && python3 manage.py migrate

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]

