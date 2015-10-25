from conexion import conexion
from login import login

def make_only_read():
    cur, conn = conexion.conectar('root','')
    query= "REVOKE ALL PRIVILEGES ON `votacionesdb`.* FROM 'guest'@'localhost'; GRANT SELECT ON `votacionesdb`.* TO 'guest'@'localhost';"
    cur.execute(query)          # Ejecutar una consulta
    conexion.cerrar_conexion(cur,conn)
