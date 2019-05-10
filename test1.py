from dijkstar import Graph, find_path

graph = Graph()
graph.add_edge(11, 2, {'cost': 1})
graph.add_edge(2, 31234, {'cost': 1})
graph.add_edge(31234, 4, {'cost': 1})
graph.add_edge(4, 5, {'cost': 1})
cost_func = lambda u, v, e, prev_e: e['cost']
print(find_path(graph, 11, 5, cost_func=cost_func))