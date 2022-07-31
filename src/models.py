from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import TIME, Column, Integer, Date, BigInteger, String, TIMESTAMP
db = SQLAlchemy()

#DB Models


class users_has_cultivos(db.Model):
    id = Column(Integer, primary_key=True)
    cultivos_id = Column(Integer)
    users_id = Column(Integer)

class cultivos(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ciclo_cultivo_id = Column(Integer)
    ambiente_cultivo_id = Column(Integer)
    fecha_inicio = Column(Date)
    fecha_final = Column(Date)
    clave_cultivo = Column(String)
    creador_id = Column(BigInteger)
    predios_id = Column(BigInteger)
    tipos_cultivo_id = Column(Integer)

class cultivos_has_biodispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    cultivos_id = Column(Integer)
    bio_dispositivos_id = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    cultivos_id = Column(Integer)


class bio_dispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    identificador = Column(String)
    tipo_biodispositivos_id = Column(Integer)
    bio_dispositivos_id = Column(BigInteger)
    dispositivos_sms_id = Column(BigInteger)
    clave = Column(String)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    recarga_saldo = Column(Date)

class sensores_has_bio_dispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    sensores_id = Column(BigInteger)
    bio_dispositivos_id = Column(BigInteger)
    updated_at = Column(TIMESTAMP)

class tipo_biodispositivos(db.Model):
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    modulos = Column(Integer)