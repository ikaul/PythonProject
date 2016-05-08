#!/usr/bin/python
class Graph():
	def __init__(self):
		self.graph = dict()
	
	def __str__(self):
		return str(self.graph)

	def addNode(self, node):
		if node not in self.graph:
			self.graph[node] = list()

	def addLink(self, node1, node2):
		self.addNode(node1)
		self.addNode(node2)
		self.graph[node1].append(node2)
	
	def routeBetweenNodes(self, start, end ):
		if start not in self.graph or end not in self.graph:
			return "Start/End node does not exist"

		visited = list()
		q = [start] 

		#Check for self loop
		if start == end:
			if start in self.graph[start]:
				return True
			else:
				return False
		while q:
			n = q.pop()
			if n not in visited:
				visited.append(n)
				if n == end:
					return True
				else:
					for node in self.graph[n]:
						q.append(node)
		return False	

g = Graph()
g.addLink('A', 'B')
print g
print g.routeBetweenNodes('A', 'D')
print g.routeBetweenNodes('A', 'A')
g.addLink('C', 'D')
print g
print g.routeBetweenNodes('A', 'D')
g.addLink('A', 'A')
g.addLink('B', 'A')
g.addLink('B', 'C')
g.addLink('D', 'A')
print g
print g.routeBetweenNodes('A', 'D')
print g.routeBetweenNodes('A', 'A')
