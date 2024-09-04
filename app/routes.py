from flask import flash, request, redirect, url_for, render_template
from sqlalchemy import func
from config import db

from app.data_service import migrar_beneficios_excel
from app.models import Beneficio




def configure_routes(app):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
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
            return redirect(url_for('index'))
        return render_template('index.html')
    
    
        
 
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
        
        return render_template('resultados.html', 
                               proceso_id=proceso_id,
                               beneficios=beneficios,
                               resumen=resumen)