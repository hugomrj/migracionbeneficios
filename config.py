import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def get_database_uri(cls):
        user = os.getenv('SQLALCHEMY_DATABASE_USER')
        password = os.getenv('SQLALCHEMY_DATABASE_PASSWORD')
        host = os.getenv('SQLALCHEMY_DATABASE_HOST')
        port = os.getenv('SQLALCHEMY_DATABASE_PORT')
        name = os.getenv('SQLALCHEMY_DATABASE_NAME')

        if not all([user, password, host, port, name]):
            raise ValueError("Missing database configuration in environment variables")

        return (
            f"mysql+mysqlconnector://{user}:"
            f"{password}@{host}:"
            f"{port}/"
            f"{name}"
        )

    @classmethod
    def get_bitacora_database_uri(cls):
        return "mysql+mysqlconnector://ususis:new210729@192.168.204.26:3306/control_usuario"




class DevelopmentConfig(Config):
    @classmethod
    def load_env(cls):
        load_dotenv('.env.dev')
        print("Loaded .env.dev")


    @classmethod
    def init_app(cls, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.get_database_uri()
        app.config['SQLALCHEMY_BINDS'] = {
            'bitacora_db': cls.get_bitacora_database_uri()
        }
        app.config['DEBUG'] = True




class ProductionConfig(Config):
    @classmethod
    def load_env(cls):
        load_dotenv('.env.prod')
        print("Loaded .env.prod")


    @classmethod
    def init_app(cls, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.get_database_uri()
        app.config['SQLALCHEMY_BINDS'] = {
            'bitacora_db': cls.get_bitacora_database_uri()
        }
        app.config['DEBUG'] = False

        # Configuración del pool de conexiones
        app.config['SQLALCHEMY_POOL_SIZE'] = 10          # Número máximo de conexiones en el pool
        app.config['SQLALCHEMY_MAX_OVERFLOW'] = 5        # Conexiones adicionales si el pool está lleno
        app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30       # Tiempo de espera antes de error si el pool está lleno
        app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800     # Reciclaje de conexiones cada 30 minutos



