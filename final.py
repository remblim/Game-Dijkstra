from dijkstar import Graph, find_path

def search_solarsystem_name(list,input):
	for systems in list:
		if systems[0] == input:
			return systems[1]
	return 'error solar system name not recognized'

def search_in_list(list,input):
	for item in list:
		if item[0] == input:
			return item[0]

def making_graph(jumpgates):
	import time
	start_time = time.time()
	import csv
	import json
	jumpgates = json.loads(jumpgates)
	graph = Graph.unmarshal('standard_graph')
	for row in jumpgates:
		print(row[0])
		print(row[1])
		graph.add_edge(row[0],row[1], {'cost': 1})
		graph.add_edge(row[1],row[0], {'cost': 1})
	
	graph.marshal('system_graph')
	print(time.time()-start_time)
	return 'Graph has been made and saved!!!'

def route_planning(start,end):
	graph = Graph.unmarshal('system_graph')
	#find the path
	cost_func = lambda u, v, e, prev_e: e['cost']
	path = find_path(graph, start, end, cost_func=cost_func)
	return path
	
def get_character_location(character):
	print(character)
	return 'E3UY-6'
	
def set_autopilot(systems):
	print(systems)

def main(string):
	input = string.split(' ')
	if input[0] == '!routeplan':
		#format !routeplan Startsystem Endsystem
		route, edges, cost, total_jumps = route_planning(input[1],input[2])
		return 'The shortest route is ' + str(total_jumps) + ' jumps long if you follow ' + ', '.join(route)
	elif input[0] == '!autopilot':
		character = string.split(',')[1]
		string = string.split(',')[0].split(' ')
		print(string)
		route, edges, cost, total_jumps = route_planning(get_character_location(character),string[1])
		set_autopilot(route)
		return 'Autopilot has been set with ' + str(total_jumps) + ' to go!'
		
if __name__ == "__main__":
	jumpbridges = [['Elonaya','K4YZ-Y']]
	import json
	dict = json.dumps(jumpbridges)
	making_graph(dict)
	input = input('data?')
	print(main(input))