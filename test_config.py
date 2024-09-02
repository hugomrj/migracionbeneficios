from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear una instancia de Flask y configurar la aplicación
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar SQLAlchemy con la configuración de la aplicación
db = SQLAlchemy(app)

@app.route('/')
def index():
    try:
        # Intentar conectar a la base de datos
        with db.engine.connect() as connection:
            return "Conexión a la base de datos exitosa!"
    except Exception as e:
        return f"Error al conectar a la base de datos: {e}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)