#!/usr/bin/python
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class SegmentTree():
	def __init__(self, arr):
		self.root = None
		self.arr = arr
		self.buildTree(self.root, 0, len(arr) - 1)
		self.sum(self.root)

	def buildTree(self, node, start, end):
		if start < end:
			print str(start) + "," + str(end)
			middle = start + int((end - start) / 2 )
			if node == None:
				node = Node()
			self.buildTree(node.left, start, middle)
			self.buildTree(node.right, middle + 1, end)
		else:
			print "Data:" + str(self.arr[start])
			node = Node(self.arr[start])

	def sum(self, node):
		if node == None:
			return 0
		elif node.left == None and node.right == None:
			return node.data
		elif node.left == None:
			return self.sum(node.right)
		elif node.right == None:
			return self.sum(node.left)
		else:
			return sum(node.left) + sum(node.right)

	def preOrderTraversal(self, node=None):
		ret = ""
		if node != None:
			ret += str(node.data)
		else:
			return ret
		if node.left != None:
			ret += self.preOrderTraversal(node.left)

		if node.right != None:
			ret += self.preOrderTraversal(node.right)
		return ret

	def __str__(self):
		return self.preOrderTraversal(self.root)


arr = [x for x in range(10)]
st = SegmentTree(arr)

print st.root
