import pandas as pd
import pymysql
from config import get_db_connection



def migrar_beneficios_excel(file):
    
    
    """Procesa el archivo Excel y migra los datos a la base de datos."""
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Conectar a la base de datos
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            for index, row in df.iterrows():
                
                print(f"Cédula: {row['cedula']}")
                
                # Construir la consulta SQL para insertar los datos en la tabla
                sql = """
                INSERT INTO nombre_de_tu_tabla (columna1, columna2, columna3, ...)
                VALUES (%s, %s, %s, ...)
                """
                # Ejecutar la consulta con los valores correspondientes
                # cursor.execute(sql, (row['columna1'], row['columna2'], row['columna3'], ...))
        
        # Confirmar los cambios en la base de datos
        connection.commit()
    finally:
        connection.close()
