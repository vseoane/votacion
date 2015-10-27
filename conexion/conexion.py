import pymysql

NOMBRE_DB = 'votacionesdb'
HOST = '127.0.0.1'
PORT = 3306
USER = 'guest'
PASSWORD = ''

def conectar(usr, passw):
    conn = pymysql.connect(host=HOST,port=PORT,user=usr,passwd=passw,db=NOMBRE_DB)
    cur = conn.cursor()
    return cur, conn


def cerrar_conexion(cur, conn):
    cur.close()
    conn.close()
