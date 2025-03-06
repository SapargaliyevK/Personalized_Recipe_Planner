import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG') or True
    # Add any other configuration variables as needed, such as database settings or API keys.