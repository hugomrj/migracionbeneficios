
from datetime import datetime
from config import db

class Bitacora(db.Model):
    __bind_key__ = 'bitacora_db' 
    __tablename__ = 'bitacora'
    
    id_bitacora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, nullable=True)  # Mapeo de ID_USUARIO
    id_form = db.Column(db.Integer, nullable=True)     # Mapeo de ID_FORM
    descrip = db.Column(db.Text, nullable=True)        # Mapeo de DESCRIP    
    fecha = db.Column(db.DateTime, default=datetime.now)
