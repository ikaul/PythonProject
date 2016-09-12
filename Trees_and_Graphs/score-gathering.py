#!/usr/bin/python

class Node(object):
	def __init__(self, info):
		self.info = info
		self.counter = 1 
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.info) + ":" + str(self.counter)

class Tree(object):
	def __init__(self):
		self.root = None

	def addNode(self, data):
		if self.root == None:
			self.root = Node(data)
		else:
			current = self.root
			while(1):
				if data < current.info:
					if current.left == None:
						current.left = Node(data)
						return True
					else:
						current = current.left
				elif data > current.info:
					if current.right == None:
						current.right = Node(data)
						return True
					else:
						current = current.right
				else:
					current.counter += 1
					return True

	def to_string(self, node):
		if node == None:
			return
		print_str = str(node)
		if node.left != None:
			print_str += self.to_string(node.left)
		elif node.right != None:
			print_str += self.to_string(node.right)
		else:
			return print_str


        def to_string(self, node):
		print_str = ""
                if node is not None:
                        print_str += str(node)
			print_str += ","
                        print_str += self.to_string(node.left)
			print_str += ","
                        print_str += self.to_string(node.right)
		else:
			return ""
		return print_str 

	def __str__(self):
		return self.to_string(self.root)

t = Tree()
arr = [4, 2, 5, 5, 6, 1, 4]
for x in arr:
	t.addNode(x)

print t
