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
	return 'error system not found so can not produce number'

#search the first result in the list of all system id's that is the same as the input and return the system name, added so it can also use lists
def search_solarsystem_name(list,input):
	output = []
	for number in input:
		for systems in list:
			if int(systems[0]) == number:
				output.append(systems[1])
				break
	if output == []:
		return 'error solar system name not recognized'
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
	path = find_path(graph, int(start), int(end), cost_func=cost_func)
	return path
	
def get_character_location(character):
	print(character)
	return 'E3UY-6'
	
def set_autopilot(systems)
	print(systems)

def main(string):
	input = string.split(' ')
	if input[0] == '!routeplan':
		#route from start to finish
		#!route startsystem finishsystem
		system_graph = loading_graph()
		start_system = search_solarsystem_number(solar_systems, input[1])
		#error giving
		if start_system.split(' ')[0] == 'error':
			return start_system
		end_system = search_solarsystem_number(solar_systems, input[2])
		#error giving
		if end_system.split(' ')[0] == 'error':
			return end_system
		path = route_planning(system_graph,start_system,end_system)
		jumps = search_solarsystem_name(solar_systems, path.nodes)
		return jumps
	elif input[0] == '!routeset':
		#route planning with autopilot
		#!routeset endsystem,character
		system_graph = loading_graph()
		start_system = get_character_location(string.split(',')[1])
		start_system = search_solarsystem_number(solar_systems, start_system)
		#error handling
		if start_system.split(' ')[0] == 'error':
			return start_system
		end_system = search_solarsystem_number(solar_systems, string.split(' ')[1].split(',')[0])
		#error handling
		if end_system.split(' ')[0] == 'error':
			return end_system
		path = route_planning(system_graph,start_system,end_system)
		jumps = search_solarsystem_name(solar_systems, path.nodes)
		return jumps
	elif input[0] == '!routemakegraph':
		system_graph = making_graph()
		saving_graph(system_graph)
	else:
		return 'Geek you have a problem, command not recognized!'

if __name__ == "__main__":
	data = input('hello')
	print(main(data))