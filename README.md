# TeamUP test task

### Инструкция по запуску:

      Пример файла с переменными окружения находится в app/.env.example

1. `$ cd teamup-iqtest_api`


2. Создать в `app/` файл с переменными окружения(.env) и обязательно установить:
   * DJANGO_SECRET_KEY
   * ALLOWED_HOSTS: Можно скопировать из `.env.example`
   * POSTGRES_URL: `postgres://<USER>:<YOUR_PASSWORD>@postgres_db:5432/<YOUR_DB_NAME>`, либо скопировать из `.env.example`
   * DEBUG: `True` или `False` 
   * POSTGRES_USER=<USER>
   * POSTGRES_PASSWORD=<YOUR_PASSWORD>
   * POSTGRES_HOST=postgres_db
   * POSTGRES_PORT=5432
   * POSTGRES_DB=<YOUR_DB_NAME>

   Пример файла с переменными окружения находится в `./app/.env`


3. После установки переменных окружения, выйти в корень проекта и выполнить команду `make up`. Поднимутся 3 Docker-контейнера:
   * Postgres
   * Django
   * Swagger-UI
4. Перейти в Swagger-UI по `localhost:8080` or `127.0.0.1:8080`. 


### Описание

Небольшое API для создания теста с уникальным логином и возможностью сохранить результаты 2-ух тестов: IQ и EQ.
При создании теста возвращается уникальный логин, который можно использовать доя сохранения результатов по двум тестам.
Более подробная документация доступна в SwaggerUI.
