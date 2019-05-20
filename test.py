import csv
#Dijkstar uses Dijkstra algorithm to plan shortest path. For info https://youtu.be/GazC3A4OQTE
from dijkstar import Graph, find_path

#import all system id's and system names, discard the rest of useless information
solar_systems = []
with open('mapSolarSystems.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for index,row in enumerate(reader):
		if index > 0:
			solar_systems.append(row[2:4])

#search the first result in the list of all systems that is the same as the input and return the system number
def search_solarsystem_number(list, input):
	for items in list:
		if items[1] == input:
			return items[0]

#search the first result in the list of all system id's that is the same as the input and return the system name, added so it can also use lists
def search_solarsystem_name(list,input):
	output = []
	for number in input:
		for systems in list:
			if int(systems[0]) == number:
				output.append(systems[1])
				break
	return output

def loading_graph():
	system_graph = Graph.unmarshal('system_graph')
	return system_graph
	
def saving_graph(system_graph):
	system_graph.marshal('system_graph')
	
def making_graph():
	#import all jump connections between systems, only has the system id's
	gates = []
	with open('mapSolarSystemJumps.csv','r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for index,row in enumerate(reader):
			if index > 0:
				gates.append(row[2:4])
				
	jump_gates=[]
	with open('jump_gates.txt','r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for index,row in enumerate(reader):
			jump_gates.append([search_solarsystem_number(solar_systems,row[0]),search_solarsystem_number(solar_systems,row[1])])
	#Create the graph for Dijkstra
	graph = Graph()
	#Add all gates to the graph
	for row in gates:
		graph.add_edge(int(row[0]),int(row[1]), {'cost': 1})
	
	#Add jump bridges one way, then the other way so you can take both ways.
	for row in jump_gates:
		graph.add_edge(int(row[0]),int(row[1]), {'cost': 1})
		graph.add_edge(int(row[1]),int(row[0]), {'cost': 1})
	return graph
	
def route_planning(graph,start,end):
	#find the path
	cost_func = lambda u, v, e, prev_e: e['cost']
	path = find_path(graph, int(start_system), int(end_system), cost_func=cost_func)
	return path
	


if __name__ == "__main__":
	while True:
		data = input('command?')
		if data == 'q':
			break
		elif data == 'load':
			system_graph = loading_graph()
			print('loaded graph')
		elif data == 'make':
			system_graph = making_graph()
			saving_graph(system_graph)
			print('saved')
		elif data == 'route':
			#get the start system as name
			data = input('Your start system?')
			#convert start system in name to start system as ID
			start_system = search_solarsystem_number(solar_systems, data)

			#get the end system as name
			data = input('Your end system?')
			#convert end system in name to end system as ID
			end_system = search_solarsystem_number(solar_systems, data)
			#planning route
			path = route_planning(system_graph,start_system,end_system)
			#Make the system ID's back to system names
			jumps = search_solarsystem_name(solar_systems, path.nodes)
			print(jumps)