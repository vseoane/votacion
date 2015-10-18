from conexion import conexion

def contar():
    cur, conn = conexion.conectar()
    result1 = cur.execute("select count(*) from votos where opcion_voto = 1")
    result2 = cur.execute("select count(*) from votos where opcion_voto = 2")
    result3 = cur.execute("select count(*) from votos where opcion_voto = 3")
    results = {'candidato1' : result1, 'candidato2' : result2, 'en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)

#esto no se si es muy util, pero hay que poner los observados en algun lado
def contar_observados():
    cur, conn = conexion.conectar()
    result1 = cur.execute("select count(*) from votos where opcion_voto = 1 and observado = true")
    result2 = cur.execute("select count(*) from votos where opcion_voto = 2 observado = true")
    result3 = cur.execute("select count(*) from votos where opcion_voto = 3 observado = true")
    results = {'observados_candidato1' : result1, 'observados_candidato2' : result2, 'observados_en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)


