#!/usr/bin/python
import unittest

class TestLinkedListAddition(unittest.TestCase):
	def setUp(self):
		list1 = [1,6,7,0,0,1]
		list2 = [0,0,0,0,0,1]
		self.l1 = LinkedList()
		self.l2 = LinkedList()
		for i in list1:
			self.l1.insert(i)
		for i in list2:
			self.l2.insert(i)
	def testSum(self):
		self.assertEqual(self.l1.sum(self.l2), 167002)

class Node(object):
        def __init__(self, data=None, link=None):
                self.link = link
                self.info = data
        def __str__(self):
                return str(self.info)

class LinkedList(object):
        def __init__(self, head=None):
                self.head = head

        def insert(self,val):
                n = Node(val)
                n.link = self.head
                self.head = n
        def __str__(self):
                n = self.head
                ret = str(n.info)
                while n.link != None:
                        n = n.link
                        ret = ret + '->' + str(n.info)
                return ret
	def value(self):
		n = self.head
		value = n.info 
		index = 1
		while n.link != None:
			n = n.link
			index = index * 10
			value = value + n.info * index
		return value
	def sum(self, ll):
		sum = self.value() + ll.value()
		return sum

if __name__ == '__main__':
    unittest.main()
