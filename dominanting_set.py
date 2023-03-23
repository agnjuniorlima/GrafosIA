import random
gVertices = {1, 2, 3, 4, 5, 6, 7, 8}
print('Vertices no grafo = ',gVertices)
gEdges = [(0, 1),(0, 2), (0, 3), (1, 3), (2, 3), (3, 4), (4, 6), (5, 6)]
print('\nAresta no grafo = ',gEdges)
S = list()
degrees = dict()
connectedMinSet = []

while len(gVertices)!=0:
	
	def findDegrees():
	
		for vertex in gVertices:
			deg = 0
			for edge in gEdges:
				if vertex in edge:	
					deg = deg+1
				else: None
			degrees[vertex] = deg
		return degrees
	findDegrees()
	maxDegree = max(degrees.values())
	for i in degrees:
		if degrees.get(i) == maxDegree:
			S.append(i)
			maxvertex= i
			
	nbrmaxvertex = set()
	nbrmaxvertex.add(maxvertex)
	gVerticesNew = set()
	for edg in enumerate(gEdges):
		
		if edg[1][0]==maxvertex:
			nbrmaxvertex.add(edg[1][1])
		elif edg[1][1]==maxvertex:
			nbrmaxvertex.add(edg[1][0])

	connectedMinSet.append(nbrmaxvertex)
	gVerticesNew = gVertices - nbrmaxvertex
	gVertices=gVerticesNew

	for v in gEdges:
		for e in gEdges:
			if maxvertex in e:
				gEdges.remove(e)
	
	degrees = dict()
	

print('\nConjunto dominante independente mínimo no gráfico = ',set(S))
