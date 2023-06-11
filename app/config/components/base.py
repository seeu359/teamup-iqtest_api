import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8080', 'http://localhost:8080']

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
