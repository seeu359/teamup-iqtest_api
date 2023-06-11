up:
	docker-compose up -d

test:
	poetry run python3 app/manage.py test

lint:
	poetry run flake8 .

install:
	poetry install