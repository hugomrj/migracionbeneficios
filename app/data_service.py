
import re
import pandas as pd
from flask import current_app as app
from app.models import db, Beneficio




def migrar_beneficios_excel(file):
    """Procesa el archivo Excel y migra los datos a la base de datos."""
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Validar el formato de la primera columna
    validar_objeto(df)


    # Usar el contexto de la aplicación para la transacción
    with app.app_context():
        try:
            for index, row in df.iterrows():
                # Crear una instancia de Beneficio con los datos del archivo Excel
                beneficio = Beneficio(
                    cedula=row.get('cedula', 0),
                    presupues=row.get('presupues', 0),
                    devengado=row.get('devengado', 0),
                    jubilacion=row.get('jubilacion', 0),
                    judicial=row.get('judicial', 0),
                    otros=row.get('otros', 0),
                    liquido=row.get('liquido', 0),
                    mes=row.get('mes', 0),
                    anio=row.get('anio', 0),
                    codigo_concepto=row.get('codigo_concepto', 0),
                    tipo_rubro=row.get('tipo_rubro', ' '),
                    ccargo=row.get('ccargo', 0),
                    tipo_traba=row.get('tipo_traba', 0)
                )
                # Agregar la instancia a la sesión
                # db.session.add(beneficio)
            
            # Confirmar los cambios en la base de datos
            # db.session.commit()
        except Exception as e:
            # Revertir la transacción en caso de error
            db.session.rollback()
            raise e








def validar_objeto(df):
    """Recorre toda la primera columna y muestra cada valor."""
    if df.empty:
        raise ValueError("El archivo está vacío")
    
    # Recorrer y mostrar cada valor de la primera columna
    print("Contenido de la primera columna:")
    for index, value in df.iloc[:, 0].items():
        # Guardar el valor en una variable
        contenido = value
        
        # Mostrar el valor actual
        # print(f"Fila {index}: {contenido}")
        
        # Realizar la verificación del contenido
        if isinstance(contenido, str) and re.match(r"OBJETO 1\d{2}:", contenido):
            print(f"Encontrado en la fila {index}: {contenido}")