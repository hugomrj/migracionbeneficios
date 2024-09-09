from flask import Flask, logging
from app.routes import configure_routes
from config import DevelopmentConfig, ProductionConfig, db
import os

def create_app():
    # Leer el entorno desde la variable de entorno FLASK_ENV (con valor predeterminado 'development')
    config_class = os.getenv('FLASK_ENV', 'DevelopmentConfig')

    # Elegir la clase de configuración correspondiente
    if config_class == 'ProductionConfig':
        config = ProductionConfig
    else:
        config = DevelopmentConfig

    # Cargar el archivo .env correspondiente usando el método load_env de la clase de configuración
    config.load_env()

    # Crear la aplicación Flask
    app = Flask(__name__)

    # Configurar la aplicación con los valores de la configuración
    config.init_app(app)

    # Inicializar el ORM con la aplicación
    db.init_app(app)

    # Configurar las rutas
    configure_routes(app)

    # Configurar una clave secreta para sesiones (usa un valor más seguro en producción)
    app.secret_key = os.getenv('SECRET_KEY', 'mi_clave_secreta')

    # Configurar el filtro para formateo de números con puntos como separador de miles
    def format_number(value):
        try:
            return "{:,.0f}".format(value).replace(",", ".")
        except (ValueError, TypeError):
            return value  # O puedes devolver un valor predeterminado

    app.jinja_env.filters['format_number'] = format_number

    # Imprimir la URL de la base de datos configurada
    print(f"Configuración activa: {config_class}")
    print(f"URL de la base de datos: {app.config.get('SQLALCHEMY_DATABASE_URI', 'No URL configured')}")


    return app

if __name__ == '__main__':
    # Crear la aplicación Flask
    app = create_app()

    # Ejecutar la aplicación en modo de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)
