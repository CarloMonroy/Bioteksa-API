from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, TIMESTAMP
db = SQLAlchemy()

#DB Models


class users_has_cultivos(db.Model):
    id = Column(Integer, primary_key=True)
    cultivos_id = Column(Integer)
    users_id = Column(Integer)

class cultivos(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column()
    ciclo_cultivo_id = Column()
    ambiente_cultivo_id = Column()
    fecha_inicio = Column()
    fecha_final = Column()
    clave_cultivo = Column()
    creador_id = Column()
    predios_id = Column()
    tipos_cultivo_id = Column()

class cultivos_has_biodispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    cultivos_id = Column()
    bio_dispositivos_id = Column()
    created_at = Column()
    updated_at = Column()
    cultivos_id = Column()


class bio_dispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column()
    identificador = Column()
    tipo_biodispositivos_id = Column()
    bio_dispositivos_id = Column()
    dispositivos_sms_id = Column()
    clave = Column()
    updated_at = Column(TIMESTAMP)
    created_at = Column()
    recarga_saldo = Column()

class sensores_has_bio_dispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    sensores_id = Column()
    bio_dispositivos_id = Column()
    updated_at = Column()

class tipo_biodispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    tipo = Column()
    modulos = Column()