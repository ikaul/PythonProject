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

	def swapElements(self):
		#Return None if Empty List
		if self.head == None:
			return None
		#Return head if only one element
		elif self.head.link == None:
			return self.head

		#Get New Head 
		prev = self.head
		current = self.head.link
		self.head = current

		#Swap Elements
		while(1):
			next = current.link
			current.link = prev

			if next == None or next.link == None:
				prev.link = next
				return self.head
			prev.link = next.link

			prev = next
			current = prev.link
			

l = [10,20,30,40,50,60,70,80,90,100,110]
ll = LinkedList()
l1 = LinkedList()
l2 = LinkedList()

for i in l:
        ll.insert(i)
print ll
print ll.swapElements()
print ll
print l1.swapElements()
l2.insert(10)
print l2.swapElements()


