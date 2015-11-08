from conexion import conexion
from login import login
import datetime
import ntp


def make_only_read():
    cur, conn = conexion.conectar('root','')
    query= "REVOKE ALL PRIVILEGES ON `votacionesDB`.* FROM 'guest'@'localhost'; GRANT SELECT ON `votacionesDB`.* TO 'guest'@'localhost';"
    cur.execute(query)          # Ejecutar una consulta
    conexion.cerrar_conexion(cur,conn)
    print "Mesa cerrada con exito"


def hora_cierre():
    hora_actual = datetime.datetime(2015,11,8,hour=00,minute=10,second=0)

    return hora_actual


def cerrar_mesa():

    if ntp.hora() < hora_cierre():
        print "Hora actual menor a hora de cierre"
        return False
    else:
        make_only_read()
        return True






