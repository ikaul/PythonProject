#!/usr/bin/python
import sys
class Graph():
	def __init__(self):
		self.graph = dict()
		self.weight = dict()
	
	def __str__(self):
		return str(self.graph)

	def addNode(self, node):
		if node not in self.graph:
			self.graph[node] = dict()
			self.weight[node] = sys.maxsize 

	def addLink(self, node1, node2, distance=1):
		self.addNode(node1)
		self.addNode(node2)
		self.graph[node1][node2] = distance

	def distance(self, node1, node2):
		return self.graph[node1][node2]

	def shortestPath(self, start, end):
		if start not in self.graph or end not in self.graph:
			return "Start/End node does not exist"

		visited = list()
		q = [start]
		self.weight[start] = 0
		path = []
		while q:
			n = q.pop()
			if n not in visited:
				visited.append(n)
				neighbors = list(self.graph[n].keys())
				for node in neighbors:
					if node not in visited:
						q.append(node)
						new_weight = self.weight[n] + self.distance(n, node)
						if new_weight < self.weight[node]:
							self.weight[node] = new_weight
	
		#Backtrace Path from end node to start node
		path.append(start)
		min_weight = sys.maxsize
		q = [start]
		visited = []
		while q:
			n = q.pop()
			visited.append(n)
			if n == end:
				return path
			neighbors = list(self.graph[n].keys())
			for node in neighbors:
				if self.weight[node] < min_weight:
					min_weight = self.weight[node]
					next = node
				print "Node: {}, Weight: {}, MinWeight: {}".format(node, self.weight[node], min_weight)
			print next
			q.append(next)
			path.append(next)
		return path

g = Graph()
g.addLink('A', 'B', 10)
g.addLink('A', 'C', 2)
g.addLink('B', 'A', 2)
g.addLink('B', 'C', 2)
g.addLink('C', 'D', 100)
print g.shortestPath('A', 'D')
print g.weight
