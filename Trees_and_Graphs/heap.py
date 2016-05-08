#!/usr/bin/python
class Heap():
	def __init__(self, list=list()):
		self.nodes = list

	def __str__(self):
		return str(self.nodes)

	def getParent(self, index):
		return (index-1) // 2

	def getLeftChild(self, index):
		return 2 * index + 1

	def getRightChild(self, index):
		return 2 * index + 2 

	def insert(self, val):
		index = len(self.nodes)
		parent = self.getParent(index)
		self.nodes.append(val)
		while (self.nodes[index] < self.nodes[parent] and parent >= 0):
			temp = self.nodes[index]
			self.nodes[index] = self.nodes[parent]
			self.nodes[parent] = temp
			index = parent
			parent = self.getParent(parent)
	
	def removeMin(self):
		n = len(self.nodes)
		if n >= 1:
			min = self.nodes[0]
			self.nodes[0] = self.nodes[n-1]
			self.nodes.pop()
			n = len(self.nodes)
			index = 0
			left = self.getLeftChild(index)
			right = self.getRightChild(index)
			while (left < n):
				if right < n:
					#Swap with smaller value
					if self.nodes[left] < self.nodes[right]:
						print "Replace " + str(index) + " with " + str(left)
						temp = self.nodes[left]
						self.nodes[left] = self.nodes[index]
						self.nodes[index] = temp
						index = left
					else:
						print "Replace " + str(index) + " with " + str(right)
						temp = self.nodes[right]
						self.nodes[right] = self.nodes[index]
						self.nodes[index] = temp
						index = right
				else:
					if self.nodes[left] < self.nodes[index]:
						print "Replace " + str(index) + " with " + str(left)
						temp = self.nodes[left]
						self.nodes[left] = self.nodes[index]
						self.nodes[index] = temp
						index = left
					else:
						return min
				left = self.getLeftChild(index)
				right = self.getRightChild(index)
			return min
		else:
			return "Heap Empty!"	
h = Heap()
data = [5,1,8,2,6,3,9]
for i in data:
	h.insert(i)
print h

h1 = Heap()
data = [4,50,7,55,90,87,2]
for i in data:
	h1.insert(i)
print h1
print h1.removeMin()

data = [4,50,23,88,90,32,74,80]

h3 = Heap(data) 
print h3
print h3.removeMin()
print h3

data = []
h4 = Heap(data) 
print h4
print h4.removeMin()
data = [10]
h4 = Heap(data) 
print h4
print h4.removeMin()
print h4
data = [4,100,10,120,101,20,11]
h4 = Heap(data) 
print h4
print h4.removeMin()
print h4
