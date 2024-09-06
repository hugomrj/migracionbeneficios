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

class DevelopmentConfig(Config):
    @classmethod
    def load_env(cls):
        load_dotenv('.env.dev')
        print("Loaded .env.dev")

    @classmethod
    def init_app(cls, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.get_database_uri()
        app.config['DEBUG'] = True

class ProductionConfig(Config):
    @classmethod
    def load_env(cls):
        load_dotenv('.env.prod')
        print("Loaded .env.prod")

    @classmethod
    def init_app(cls, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.get_database_uri()
        app.config['DEBUG'] = False
