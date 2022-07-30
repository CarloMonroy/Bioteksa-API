from models import cultivos, cultivos_has_biodispositivos, bio_dispositivos,tipo_biodispositivos, sensores_has_bio_dispositivos, users_has_cultivos

def fill_response(user_cultivos):

    cultivos_arr = []
    response_array = []

    for cultivo in user_cultivos.items:
        query = cultivos.query.filter_by(id=cultivo.cultivos_id).first()
        cultivos_arr.append(query)

    for cultivo in cultivos_arr:
        response = {
            "nombre": cultivo.nombre,
            "ciclo_cultivo_id": cultivo.ciclo_cultivo_id,
            "ambiente_cultivo_id": cultivo.ambiente_cultivo_id,
            "fecha_inicio": cultivo.fecha_inicio,
            "fecha_final": cultivo.fecha_final,
            "clave_cultivo": cultivo.clave_cultivo,
            "creador_id": cultivo.creador_id,
            "id": cultivo.id,
            "predios_id": cultivo.predios_id,
            "tipos_cultivo_id": cultivo.tipos_cultivo_id,
            "devices": fill_devices(cultivo.id)
            }
        response_array.append(response)
    return response_array


def fill_devices(cultivo_id):

    ## En bio_dispositivos el updated_at es nullable y no tiene datos. Tienes que sacarlos de cultivos_has_biodispositivios


    bio_dispositivos_array = []
    cul_biodispositivos = cultivos_has_biodispositivos.query.filter_by(cultivos_id=cultivo_id).all()

    for cultivo in cul_biodispositivos:
        bio_id = cultivo.bio_dispositivos_id
        bio_dispositivos_query = bio_dispositivos.query.filter_by(id=bio_id).first()
        sensores_bio = sensores_has_bio_dispositivos.query.filter_by(bio_dispositivos_id=bio_id).first()
        tipo_bio = tipo_biodispositivos.query.filter_by(id=bio_dispositivos_query.tipo_biodispositivos_id).first()
        dispositivos_data = {
            "nombre": bio_dispositivos_query.nombre,
            "clave": bio_dispositivos_query.clave,
            "id": bio_dispositivos_query.id,
            "tipo_biodispositivos_id": bio_dispositivos_query.tipo_biodispositivos_id,
            "pivot": {
                "cultivos_id": cultivo.cultivos_id,
                "bio_dispositivos_id": bio_dispositivos_query.bio_dispositivos_id,
                },
            "last_log": [{
                "value_datetime": cultivo.updated_at,
                "pivot": {
                    "bio_dispositivos_id": bio_dispositivos_query.bio_dispositivos_id,
                    "sensores_id": sensores_bio.sensores_id,
                    }
                }],
            "device_type": {
                "id": tipo_bio.id,
                "nombre": bio_dispositivos_query.nombre,
                "modulos": tipo_bio.modulos
                }
            }
        bio_dispositivos_array.append(dispositivos_data)

    return bio_dispositivos_array

