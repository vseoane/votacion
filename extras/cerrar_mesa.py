import datetime
from votacion.conexion import conexion

from votacion.extras import ntp

def hora_cierre():
    hora_cierre = datetime.datetime(2015,11,17,hour=8,minute=0,second=0)
    return hora_cierre


def cerrar_mesa():

    if ntp.hora() < hora_cierre():
        print ("Hora actual menor a hora de cierre")
        return False
    else:
        print ("Mesa cerrada con exito")
        return True






