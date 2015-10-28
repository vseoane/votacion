from hashlib import sha256
from conexion import conexion


def login(usr,psw):
    if usr.isdigit():
        query = "SELECT `contrasena` FROM `usuarios_mesa` WHERE `cedula` = " + usr
        psw_db = run_query(query)
        psw_hash1 = sha256(psw).hexdigest()
        if psw_hash1 == psw_db:
            msg = ""
            return True

        else:
            print ("Usuario y/o contrasena no valida")
            return False
    else: # ingreso caracteres que no son numeros
        print ("Debe ingresar una cedula valida")
        return False



def run_query(query=""):
    cur, conn = conexion.conectar("guest","")
    cur.execute(query)          # Ejecutar una consulta
    data = None
    if query.upper().startswith('SELECT'):
        dat = cur.fetchall();
        for registro in dat:
            data = registro[0]

    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    conexion.cerrar_conexion(cur,conn)

    return data
