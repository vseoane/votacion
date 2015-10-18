import pymysql

NOMBRE_DB = 'votacionesdb'
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = ''

def conectar():
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=NOMBRE_DB)
    cur = conn.cursor()
    return cur, conn


def cerrar_conexion(cur, conn):
    cur.close()
    conn.close()
