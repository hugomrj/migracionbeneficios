import pymysql

import pymysql
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_USER = 'root'
    SQLALCHEMY_DATABASE_PASSWORD = 'admin123'
    SQLALCHEMY_DATABASE_HOST = '127.0.0.1'
    SQLALCHEMY_DATABASE_PORT = '3306'
    SQLALCHEMY_DATABASE_NAME = 'sistemabase'

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASSWORD}@"
        f"{SQLALCHEMY_DATABASE_HOST}:{SQLALCHEMY_DATABASE_PORT}/{SQLALCHEMY_DATABASE_NAME}"
    )

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_USER = 'user_prod'
    SQLALCHEMY_DATABASE_PASSWORD = 'prod_pass'
    SQLALCHEMY_DATABASE_HOST = 'prod_db_host'
    SQLALCHEMY_DATABASE_PORT = '3306'
    SQLALCHEMY_DATABASE_NAME = 'prod_database'

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASSWORD}@"
        f"{SQLALCHEMY_DATABASE_HOST}:{SQLALCHEMY_DATABASE_PORT}/{SQLALCHEMY_DATABASE_NAME}"
    )




def get_db_connection():
    """Retorna una conexión a la base de datos utilizando la configuración adecuada."""
    env = os.getenv('FLASK_ENV', 'development')
    
    if env == 'development':
        config = DevelopmentConfig()
    else:
        config = ProductionConfig()

    return pymysql.connect(
        host=config.SQLALCHEMY_DATABASE_HOST,
        user=config.SQLALCHEMY_DATABASE_USER,
        password=config.SQLALCHEMY_DATABASE_PASSWORD,
        database=config.SQLALCHEMY_DATABASE_NAME
    )
