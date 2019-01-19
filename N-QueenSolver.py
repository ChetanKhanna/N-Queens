#############################################################################################################

#### The Idea: since there are N queens and in the NxN board, each queen must be in a different row. The nodes
#### of the graph formed below represents queen in row[i], for eg. node[3] = 6 shows that queen in 3rd row is
#### in the 6th column. Since this is iterative CSP, there is no 'domain'. We randomly assign each var a value
#### and then improve its value based on the heuristic functions defined below.
 
def goalTest(assignment, graph):
	## If all assignments have heuristic value 0, goal is reached
	for var in assignment:
		if minConflictValHeuristic(var, assignment, graph) > 0:
			return False
	return True

def nextConflictedVar(assignment, graph):
	## accessing vertices and returning the first vertex which has conflicted assignment
	for n in graph.getVertices():
		if minConflictValHeuristic(n, assignment, graph) > 0:
			return n

def minConflictValHeuristic(var, assignment, graph):
	## The heuristic value = the number of queens which are in the same column as queen 'var'
	## If no queen is in same row as queen 'var', then assignment is un-conflicted
	H = 0
	for q in graph.getVertices():
		if q!=var and assignment[var] == assignment[q]:
			H += 1
	return H

def minConflictValHeuristicVal(var, assignment, graph):
	## pos contains all possible positions possible for queen 'var', which is in face all columns
	## in NxN board. To get N, we count number of vertices in the graph
	pos = [(i, list(assignment.values()).count(i)) for i in range(len(graph.getVertices()))]
	## We now sort the pos list with second element as key
	## The second element of tuple gives the count of queens located in that column -- an indirect
	## way to compute minConflictHeuristic. We then sort it, and place the queen in the col with min
	## number of queens.
	pos.sort(key = lambda x: x[1])
	## since list is sorted in ascending order, return first element
	return pos[0][0]

def iterativeSearch(assignment, graph):
	while not goalTest(assignment, graph):
		var = nextConflictedVar(assignment, graph)
		print('var selected:', var)
		val = minConflictValHeuristicVal(var, assignment, graph)
		print('val assigned:', val)
		assignment[var] = val
	return assignment

#############################################################################################################
from random import randint
import time
import graph

G = graph.Graph()
N = 1000
for i in range(N):
	G.addVertex(i)

assignment = {}
for n in G.getVertices():
	assignment[n] = randint(0,999)
print('initial assignment:', assignment)

startTime = time.clock()
newAssignment = iterativeSearch(assignment, G)
endTime = time.clock()
print('final assignment:', newAssignment)
print('Time taken to assign', N, 'queens:', endTime - startTime)