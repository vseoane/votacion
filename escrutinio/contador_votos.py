from conexion import conexion
from login.login import run_query


def contar():
    cur, conn = conexion.conectar()
    query1="select count(*) from votos where opcion_voto = 1"
    result1 = run_query(query1)
    query2="select count(*) from votos where opcion_voto = 2"
    result2 = cur.run_query(query2)
    query3="select count(*) from votos where opcion_voto = 3"
    result3 = cur.run_query(query3)
    results = {'candidato1' : result1, 'candidato2' : result2, 'en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)

#esto no se si es muy util, pero hay que poner los observados en algun lado
def contar_observados():
    cur, conn = conexion.conectar()
    query1="select count(*) from votos where opcion_voto = 1 and observado = true"
    result1 = run_query(query1)
    query2="select count(*) from votos where opcion_voto = 2 observado = true"
    result2 = cur.run_query(query2)
    query3="select count(*) from votos where opcion_voto = 3 observado = true"
    result3 = cur.run_query(query3)
    results = {'candidato1' : result1, 'candidato2' : result2, 'en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)


