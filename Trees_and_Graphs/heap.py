#!/usr/bin/python
import unittest
class Heap(object):
	def __init__(self):
		self.nodes = []

	def __str__(self):
		return str(self.nodes)

	def __len__(self):
		return len(self.nodes)

	def getParent(self, index):
		return (index-1) // 2

	def getLeftChild(self, index):
		return 2 * index + 1

	def getRightChild(self, index):
		return 2 * index + 2

	def hasParent(self, index):
		return self.getParent(index) >= 0

	def hasLeftChild(self, index):
		return self.getLeftChild(index) < len(self.nodes)

	def hasRightChild(self, index):
		return self.getRightChild(index) < len(self.nodes)

	def peek(self):
		if self.nodes:
			return self.nodes[0]
		else:
			return None

class MinHeap(Heap):
	def heapify_up(self):
		n = len(self.nodes)
		index = n - 1
		parent = self.getParent(index)
		while (self.nodes[index] < self.nodes[parent] and parent >= 0):
			temp = self.nodes[index]
			self.nodes[index] = self.nodes[parent]
			self.nodes[parent] = temp
			index = parent
			parent = self.getParent(parent)

	def heapify_down(self):
		index = 0
		left = self.getLeftChild(index)
		right = self.getRightChild(index)
		n = len(self.nodes)
		while (self.hasLeftChild(index)):
			min_child_node = left
			if right < n and self.nodes[left] > self.nodes[right]:
				min_child_node = right

			#Swap with smaller child node
			if self.nodes[index] > self.nodes[min_child_node]:
				temp = self.nodes[min_child_node]
				self.nodes[min_child_node] = self.nodes[index]
				self.nodes[index] = temp
			index = min_child_node
			left = self.getLeftChild(index)
			right = self.getRightChild(index)

	def insert(self, val):
		self.nodes.append(val)
		self.heapify_up()

	def removeMin(self):
		n = len(self.nodes)
		if n >= 1:
			min = self.nodes[0]
			self.nodes[0] = self.nodes[n-1]
			self.nodes.pop()
			self.heapify_down()
			return min
		else:
			return "MinHeap Empty!"

	def poll(self):
		if len(self.nodes) >= 1:
			return self.removeMin()

class MaxHeap(Heap):
	def heapify_up(self):
		n = len(self.nodes)
		index = n - 1
		parent = self.getParent(index)
		while (self.nodes[index] > self.nodes[parent] and parent >= 0):
			temp = self.nodes[index]
			self.nodes[index] = self.nodes[parent]
			self.nodes[parent] = temp
			index = parent
			parent = self.getParent(parent)

	def heapify_down(self):
		n = len(self.nodes)
		index = 0
		left = self.getLeftChild(index)
		right = self.getRightChild(index)
		while (self.hasLeftChild(index)):
			max_child_node = left
			#Check which child node is bigger
			if right < n and self.nodes[left] < self.nodes[right]:
				max_child_node = right

			#Swap with bigger child node
			if self.nodes[index] < self.nodes[max_child_node]:
				temp = self.nodes[index]
				self.nodes[index] = self.nodes[max_child_node]
				self.nodes[max_child_node] = temp
			index = max_child_node
			left = self.getLeftChild(index)
			right = self.getRightChild(index)

	def insert(self, val):
		self.nodes.append(val)
		self.heapify_up()

	def removeMax(self):
		n = len(self.nodes)
		if n >= 1:
			max = self.nodes[0]
			self.nodes[0] = self.nodes[n-1]
			self.nodes.pop()
			self.heapify_down()
			return max
		else:
			return "MaxHeap Empty!"

	def poll(self):
		if len(self.nodes) >= 1:
			return self.removeMax()

class RunningMedian(object):
	def __init__(self):
		self.low = MaxHeap()
		self.high = MinHeap()

	def insert(self, value):
		if len(self.low) == 0 or value < self.low.peek():
			self.low.insert(value)
		else:
			self.high.insert(value)
		self.rebalance()

	def rebalance(self):
		n_low = len(self.low)
		n_high = len(self.high)
		if n_low < n_high:
			if n_high - n_low > 1:
				 self.low.insert(self.high.poll())
		else:
			if n_low - n_high > 1:
				self.high.insert(self.low.poll())

	def median(self):
		n_low = len(self.low)
		n_high = len(self.high)
		if n_low == n_high:
			return float(self.low.peek() + self.high.peek()) / 2
		elif n_low > n_high:
			return self.low.peek()
		elif n_low < n_high:
			return self.high.peek()


class Test_HeapMinMax(unittest.TestCase):
	def setUp(self):
		self.h_min = MinHeap()
		self.h_max = MaxHeap()
		self.median = RunningMedian()
		self.data = [5,1,8,2,6,3,9]
		self.h_min_large = MinHeap()
		self.h_max_large = MaxHeap()
		self.median_large = RunningMedian()
		for i in self.data:
			self.h_min.insert(i)
			self.h_max.insert(i)
			self.median.insert(i)
		for i in range(1000):
			self.h_min_large.insert(i)
			self.h_max_large.insert(i)
			self.median_large.insert(i)
	def test_maxHeap(self):
		self.assertEqual(len(self.h_max), len(self.h_max.nodes))
		self.assertEqual(self.h_max.peek(), 9)
		self.assertEqual(str(self.h_max), str([9, 6, 8, 1, 2, 3, 5]))
		self.assertEqual(self.h_max.removeMax(), 9)
		self.assertEqual(str(self.h_max), str([8, 6, 5, 1, 2, 3]))
		for i in range(6):
			self.h_max.removeMax()
		self.assertEqual(self.h_max.removeMax(), "MaxHeap Empty!")
		for i in range(1000):
			self.assertEqual(self.h_max_large.removeMax(), 999 - i)
		self.assertEqual(self.h_max_large.removeMax(), "MaxHeap Empty!")
	def test_minHeap(self):
		self.assertEqual(len(self.h_min), len(self.h_min.nodes))
		self.assertEqual(self.h_min.peek(), 1)
		self.assertEqual(str(self.h_min), str([1, 2, 3, 5, 6, 8, 9]))
		self.assertEqual(self.h_min.removeMin(), 1)
		self.assertEqual(str(self.h_min), str([2, 5, 3, 9, 6, 8]))
		for i in range(6):
			self.h_min.removeMin()
		self.assertEqual(self.h_min.removeMin(), "MinHeap Empty!")
		for i in range(1000):
			self.assertEqual(self.h_min_large.removeMin(), i)
		self.assertEqual(self.h_min_large.removeMin(), "MinHeap Empty!")
	def test_runningMedian(self):
		self.assertEqual(self.median.median(), 5.0)
		self.median.insert(6)
		self.assertEqual(self.median.median(), 5.5)
		self.assertEqual(self.median_large.median(), 499.5)
		self.median_large.insert(1000)
		self.assertEqual(self.median_large.median(), 500)

unittest.main()
