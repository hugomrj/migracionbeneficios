import logging
import os
from run import create_app

# Establecer FLASK_ENV antes de crear la aplicación
os.environ['FLASK_ENV'] = 'ProductionConfig'

# Crear la aplicación
app = create_app()

# Configuración del logging
if app.debug:
    app.logger.info("La aplicación está en modo de depuración.")
else:
    app.logger.info("La aplicación está en modo de producción.")

# Solo configura el logging si no está en modo de depuración
if not app.debug:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

# Configurar el formato del logging
handler = logging.StreamHandler()  # Usa FileHandler si quieres escribir en un archivo
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Registrar información sobre la configuración y la base de datos
app.logger.info(f"Config wsgi : {os.getenv('FLASK_ENV', 'No FLASK_ENV configured')}")
app.logger.info(f"URL de la base de datos: {app.config.get('SQLALCHEMY_DATABASE_URI', 'No URL configured')}")

# Gunicorn usa el archivo WSGI para servir la aplicación
if __name__ == "__main__":
    app.run()
