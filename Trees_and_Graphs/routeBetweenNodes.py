#!/usr/bin/python
import unittest
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

class GraphRouteTests(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.addLink('A', 'B')
		self.g.addNode('C')
		self.g.addLink('B', 'D')
	def test_validInput(self):
		self.assertTrue(self.g.routeBetweenNodes('A', 'D'))
		self.assertFalse(self.g.routeBetweenNodes('A', 'A'))
		self.assertFalse(self.g.routeBetweenNodes('A', 'C'))
	def test_invalidInput(self):
		self.assertEqual("Start/End node does not exist", self.g.routeBetweenNodes('A', None))
	def test_boundaryInput(self):
		self.g.addLink('A', 'A')
		self.assertTrue(self.g.routeBetweenNodes('A', 'A'))
		self.g.addLink('D', 'C')
		self.g.addLink('C', 'A')
		self.assertTrue(self.g.routeBetweenNodes('D', 'B'))
		self.assertTrue(self.g.routeBetweenNodes('C', 'B'))

unittest.main()
