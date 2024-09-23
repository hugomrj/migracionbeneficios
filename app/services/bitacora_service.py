
from app.models.beneficio_model import Beneficio
from app.models.bitacora_model import Bitacora
from config import db


from sqlalchemy.orm.exc import NoResultFound

def guardar_bitacora(usuario, form, proceso_id):
    # Obtener el registro correspondiente al proceso_id
    try:
        # Asumiendo que solo hay un registro por proceso_id
        beneficio = Beneficio.query.filter_by(proceso_id=proceso_id).first()
        
        if beneficio:
            # Obtener los valores de mes, anio, codigo_concepto y planilla
            mes = beneficio.mes
            anio = beneficio.anio
            codigo_concepto = beneficio.codigo_concepto
            planilla = beneficio.planilla
            
            # Ahora puedes usar estos valores para cualquier propósito, por ejemplo, al guardar en la bitacora
            descripcion = (
                f"Migracion de beneficios de excel a mysql:  "
                f"Mes: {mes}, Año: {anio}, Concepto: {codigo_concepto}, Planilla: {planilla}"
            )
            
            # Llamar a la función para guardar en la bitacora
            bitacora = Bitacora(
                id_usuario=usuario,
                id_form=form,
                descrip=descripcion
            )
            db.session.add(bitacora)
            db.session.commit()
        else:
            print(f"No se encontró ningún registro para proceso_id: {proceso_id}")
    except NoResultFound:
        print(f"No se encontró ningún registro para proceso_id: {proceso_id}")



