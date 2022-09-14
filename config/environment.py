import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/url_shortener_db')
secret = os.getenv('SECRET', 'a suitable secret')