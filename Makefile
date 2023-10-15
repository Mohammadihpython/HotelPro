.PHONY: all server worker beat
all: server worker beat

server:
    python manage.py migrate && python manage.py runserver

worker:
    python -m celery -A project_name worker --loglevel info

beat:
    python -m celery -A project_name beat --loglevel info