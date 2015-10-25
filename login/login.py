from hashlib import sha256
from conexion import conexion


def login(usr,psw):
    query = "SELECT `contrasena` FROM `usuarios_mesa` WHERE `cedula` = " + usr
    psw_db = run_query(query)
    psw_hash1 = sha256(psw).hexdigest()

    if psw_hash1 == psw_db:
        msg = ""
        return (True, msg)

    else:
         msg = "Usuario y/o contrasena no valida"
         return (False, msg)


def run_query(query=""):
    cur, conn = conexion.conectar("guest","")
    cur.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = ''.join(map(str, (cur.fetchone())))   # Traer los resultados de un select y quitar parentesis con join()
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    conexion.cerrar_conexion(cur,conn)

    return data
