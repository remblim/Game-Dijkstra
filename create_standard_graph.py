import csv
from dijkstar import Graph, find_path
import time

start_time = time.time()

#initialize graph
graph = Graph()

def search_solarsystem_name(list,input):
	for systems in list:
		if int(systems[0]) == int(input):
			return systems[1]
	return 'error solar system name not recognized'

#get all the normal jumps in the graph
solar_systems = []
with open('mapSolarSystems.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for index,row in enumerate(reader):
		if index > 0:
			solar_systems.append([row[2],row[3]])

print('loaded solar systems')

with open('mapSolarSystemJumps.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for index,row in enumerate(reader):
		if index > 0:
			start_system = search_solarsystem_name(solar_systems,row[2])
			end_system = search_solarsystem_name(solar_systems,row[3])
			graph.add_edge(start_system,end_system, {'cost': 1})

graph.marshal('standard_graph')
print('graph has been saved')
print(time.time()-start_time)