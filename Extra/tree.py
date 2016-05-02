#!/usr/bin/python

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
                self.right = None

	def __str__(self):
		return str(self.data)

class BST():
	def __init__(self):
		self.root = None

	def create(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			current = self.root
			while 1:
				if val < current.data:
					if current.left:
						current = current.left
					else:
						current.left = Node(val)
						break
				elif val > current.data:
					if current.right:
						current = current.right
					else:
						current.right = Node(val)
						break
				else:
					break
	def inorder(self, node):
		if node is not None:
			self.inorder(node.left)
			print node.data
			self.inorder(node.right)
	def postorder(self, node):
		if node is not None:
			self.postorder(node.left)
			self.postorder(node.right)
			print node.data
	def preorder(self, node):
		if node is not None:
			print node.data
			self.preorder(node.left)
			self.preorder(node.right)


b = BST()
data = [5,5,5,5,4,10,2,1,18,20]
for i in data:
	b.create(i)


b.preorder(b.root) 
