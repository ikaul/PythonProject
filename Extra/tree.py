#!/usr/bin/python
import sys
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

def checkBST_recursive(root, min, max):
	if root == None:
		return True
	elif root.data > min and root.data < max:
		return checkBST_recursive(root.left, min, root.data) and checkBST_recursive(root.right, root.data, max)
	else:
		return False

def checkBST(root):
	return checkBST_recursive(root, -1 * sys.maxint, sys.maxint)

b = BST()
data = [5,5,5,5,4,10,2,1,18,20]
for i in data:
	b.create(i)

print checkBST(b.root)
b.preorder(b.root)
