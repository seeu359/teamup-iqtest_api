import os
from dj_database_url import config


DATABASE_CONFIG = config(
    conn_max_age=600,
    conn_health_checks=True,
    default=os.getenv('POSTGRES_URL'),
)

DATABASES = {
    'default': DATABASE_CONFIG,
}
