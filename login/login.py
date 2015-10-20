from conexion import conexion
import hashlib
from interfaz import ventana_principal
from conexion import conexion

def login(usr,psw):
    query = "SELECT `contrasena` FROM `usuarios_mesa` WHERE `cedula` = " + usr
    psw_db = run_query(query)
    psw_hash1 = hashlib.sha256(psw).hexdigest()
    print psw_hash1
    print psw_db

    if psw_hash1 == psw_db:
        #aca tenemos que llamar a ventana_principal.py
        #esto es solo una prueba
        print usr, psw

    else:
         print "Usuario y/o contrasena no valida"
         #llamar a ventana de login


def run_query(query=''):
    cur, conn = conexion.conectar()
    cur.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = ''.join(map(str, (cur.fetchone())))   # Traer los resultados de un select y quitar parentesis con join()
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    conexion.cerrar_conexion(cur,conn)

    return data
