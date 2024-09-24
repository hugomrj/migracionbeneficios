from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    user = 'ususis'
    password = 'new210729'
    host = '192.168.204.26'
    port = '3306'
    name = 'control_usuario'

    try:
        # Crear la conexión
        connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=name
        )
        if connection.is_connected():
            return "Conexión exitosa a la base de datos."
    except Error as e:
        return f"Error al conectar a la base de datos: {e}"
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
