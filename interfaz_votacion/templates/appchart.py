from graph_tools import graphs
graph = graphs.BarGraph('pBar')
graph.values = [(50, 100), (60, 100), (70, 100)]
graph.labels = ['cats', 'dogs', 'birds']
print graph.create()
