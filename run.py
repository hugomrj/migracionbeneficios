from flask import Flask
from config import DevelopmentConfig, ProductionConfig, db
from app.routes import configure_routes
import os

def create_app():
    # Leer el entorno desde la variable de entorno (con valor predeterminado 'DevelopmentConfig')
    config_class = os.getenv('FLASK_CONFIG', 'DevelopmentConfig')

    # Crear la aplicación Flask
    app = Flask(__name__)

    # Cargar la configuración basada en el entorno
    if config_class == 'ProductionConfig':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Inicializar el ORM con la aplicación
    db.init_app(app)

    # Configurar las rutas
    configure_routes(app)

    # Configurar una clave secreta para sesiones (usa un valor más seguro en producción)
    app.secret_key = os.getenv('SECRET_KEY', 'mi_clave_secreta')

    # Configurar el filtro para formateo de números
    def format_number(value):
        try:
            return "{:,}".format(value)
        except (ValueError, TypeError):
            return value  # O puedes devolver un valor predeterminado

    app.jinja_env.filters['format_number'] = format_number

    # Imprimir la URL de la base de datos configurada
    print(f"Configuración activa: {config_class}")
    print(f"URL de la base de datos: {app.config['SQLALCHEMY_DATABASE_URI']}")

    return app

if __name__ == '__main__':
    # Crear la aplicación Flask
    app = create_app()
    
    # Ejecutar la aplicación en modo de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)
