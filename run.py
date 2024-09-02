from flask import Flask
from config import Config
from app.routes import configure_routes

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Cargar la configuración desde la clase Config
app.config.from_object(Config)

# Configurar rutas
configure_routes(app)

# Configurar la clave secreta directamente (opcional si ya está en config.py)
app.secret_key = 'mi_clave_secreta'

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)
    