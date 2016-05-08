#!/usr/bin/python
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
		
list1 = [1,6,7,0,0,1]
list2 = [0,0,0,0,0,1]
l1 = LinkedList()
l2 = LinkedList()
for i in list1:
        l1.insert(i)
for i in list2:
        l2.insert(i)

print l1.value()
print l1.sum(l2)
