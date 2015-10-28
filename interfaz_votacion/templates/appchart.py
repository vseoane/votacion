from escrutinio.contador_votos import contar
from graph_tools import graphs

graph = graphs.BarGraph('vBar')
results = contar()
graph.values = [results["candidato1"],results["candidato2"],results["en_blanco"]]
graph.labels = ['Candidato 1', 'Candidato 1', 'En blanco']
print (graph.create())
