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
	def k2end(self,k):
		p1 = self.head
		p2 = self.head
		count = 1 
		while p2.link != None:
			count += 1
			p2 = p2.link
		p2 = self.head
		if count < k:
			return "K is bigger than Linked List"
		for i in range(count-k):
			if p2.link != None:
				p2 = p2.link
		while p2.link != None:
			p1 = p1.link
			p2 = p2.link
		self.head = p1
		return str(self) 

l = [10,20,30,40,50,60,70,80,90,100,110]
ll = LinkedList()
l1 = LinkedList()
l2 = LinkedList()
l3 = LinkedList()
for i in l:
        ll.insert(i)
        l1.insert(i)
        l2.insert(i)
        l3.insert(i)
print ll

print l1.k2end(10)
print l2.k2end(12)
print l3.k2end(6)
