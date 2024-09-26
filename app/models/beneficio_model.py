from flask_sqlalchemy import SQLAlchemy
from config import db


class Beneficio(db.Model):
    __tablename__ = 'beneficios_migracion'
    
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, nullable=False, default=0)
    letra = db.Column(db.String(2), nullable=True)
    
    presupues = db.Column(db.Integer, nullable=False, default=0)
    devengado = db.Column(db.Integer, nullable=False, default=0)
    jubilacion = db.Column(db.Integer, nullable=False, default=0)
    judicial = db.Column(db.Integer, nullable=False, default=0)
    otros = db.Column(db.Integer, nullable=False, default=0)
    liquido = db.Column(db.Integer, nullable=False, default=0)
    
    mes = db.Column(db.Integer, nullable=False, default=0)
    anio = db.Column(db.Integer, nullable=False, default=0)
    codigo_concepto = db.Column(db.Integer, nullable=False, default=0)
    planilla = db.Column(db.Integer, nullable=False, default=0)
    
    tipo_rubro = db.Column(db.String(1), nullable=False, default=' ')
    ccargo = db.Column(db.Integer, nullable=False, default=0)
    tipo_traba = db.Column(db.Integer, nullable=False, default=0)
    proceso_id = db.Column(db.String(50), nullable=True)

    id_usuario = db.Column(db.Integer, nullable=False, default=0)

