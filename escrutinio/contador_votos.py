from conexion import conexion
from login import login


def contar():
    cur, conn = conexion.conectar("guest", "")
    query1 = "SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 1"
    result1 = login.run_query(query1)
    query2 = "SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 2"
    result2 = login.run_query(query2)
    query3 = "SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 3"
    result3 = login.run_query(query3)
    results = {'candidato1' : result1, 'candidato2' : result2, 'en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)

#esto no se si es muy util, pero hay que poner los observados en algun lado
def contar_observados():
    cur, conn = conexion.conectar()
    query1="SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 1 AND `observado` = TRUE"
    result1 = login.run_query(query1)
    query2="SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 2 AND `observado` = TRUE"
    result2 = login.run_query(query2)
    query3="SELECT COUNT(*) FROM `votos` WHERE `opcion_voto` = 3 AND `observado` = TRUE"
    result3 = login.run_query(query3)
    results = {'candidato1' : result1, 'candidato2' : result2, 'en_blanco' : result3}
    return results
    cerrar_conexion(cur,conn)


