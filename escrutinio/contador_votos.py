from conexion import conexion

def contar():
    cur, conn = conexion.conectar()
    cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    print()
    for row in cur:
        print(row)

