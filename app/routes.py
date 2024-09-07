from flask import flash, request, redirect, url_for, render_template
from sqlalchemy import func
from config import db

from app.data_service import migrar_beneficios_excel
from app.models import Beneficio




def configure_routes(app):
    
    @app.route('/migracion', methods=['GET', 'POST'])
    def migracion():
        if request.method == 'POST':
            file = request.files.get('file')
            if file and file.filename.endswith('.xlsx'):
                try:
                    proceso_id = migrar_beneficios_excel(file)
                    
                    print(f"Redirigiendo a ver_resultados con proceso_id: {proceso_id}")
                    
                    return redirect(url_for('ver_resultados', proceso_id=proceso_id))
                    
                    #flash('Archivo procesado y datos migrados con éxito.', 'success')
                except Exception as e:
                    flash(f'Ocurrió un error al procesar el archivo: {e}', 'danger')
            else:
                flash('Por favor, carga un archivo Excel válido.', 'warning')
            return redirect(url_for('migracion'))
        return render_template('migracion.html')
    
    
        
 
    @app.route('/resultados/<proceso_id>')
    def ver_resultados(proceso_id):
        # Consultar los beneficios individuales
        beneficios = Beneficio.query.filter_by(proceso_id=proceso_id).all()
        
        # Consultar los totales agregados
        resumen = db.session.query(
            func.sum(Beneficio.presupues).label('presupuesto'),
            func.sum(Beneficio.devengado).label('devengado'),
            func.sum(Beneficio.jubilacion).label('jubilacion'),
            func.sum(Beneficio.liquido).label('liquido')
        ).filter_by(proceso_id=proceso_id).first()
        
        
        # Contar la cantidad de registros
        cantidad_registros = Beneficio.query.filter_by(proceso_id=proceso_id).count()        
        
        
        return render_template('resultados.html', 
                            proceso_id=proceso_id,
                            beneficios=beneficios,
                            resumen=resumen,
                            cantidad_registros=cantidad_registros)    
        
    
    
        
    @app.route('/confirmar/<proceso_id>', methods=['GET'])
    def confirmar_migracion(proceso_id):
        # Solo muestra el mensaje de éxito y redirige a la página principal
        flash('Archivo procesado y datos migrados con éxito.', 'success')
        return redirect(url_for('migracion'))
        


    @app.route('/eliminar/<proceso_id>', methods=['POST'])
    def eliminar_registros(proceso_id):
        try:
            # Eliminar los registros con el proceso_id dado
            Beneficio.query.filter_by(proceso_id=proceso_id).delete()
            db.session.commit()
            flash('Migracion cancelada.', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error cancelar migracion: {e}', 'danger')
        
        return redirect(url_for('migracion'))         
    
    
    
    