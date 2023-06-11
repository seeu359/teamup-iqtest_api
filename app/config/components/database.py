import os
from pathlib import Path
from dj_database_url import config


CI = os.getenv('CI') == 'True'

SQLITE_DIR = Path(__file__).resolve().parent.parent

SQLITE_URL = os.path.join(SQLITE_DIR, 'db.sqlite')

DATABASE_URL = os.getenv('DATABASE_URL') if not CI else SQLITE_URL

DATABASE_CONFIG = config(
    conn_max_age=600,
    conn_health_checks=True,
    default=os.getenv('DATABASE_URL'),
)

DATABASES = {
    'default': DATABASE_CONFIG,
}
