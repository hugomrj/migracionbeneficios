from flask import flash, request, redirect, url_for, render_template

from app.data_service import migrar_beneficios_excel




def configure_routes(app):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            file = request.files.get('file')
            if file and file.filename.endswith('.xlsx'):
                try:
                    migrar_beneficios_excel(file)
                    flash('Archivo procesado y datos migrados con éxito.', 'success')
                except Exception as e:
                    flash(f'Ocurrió un error al procesar el archivo: {e}', 'danger')
            else:
                flash('Por favor, carga un archivo Excel válido.', 'warning')
            return redirect(url_for('index'))
        return render_template('index.html')