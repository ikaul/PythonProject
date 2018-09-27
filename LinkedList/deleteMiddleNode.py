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
                        ret = str(n.info) + '->' + ret
                return ret

        def delMiddleNode(self, val):
                n = self.head
		found = None
		prev = None
                while n != None:
			if n.info == val:
				found = 1 
				break
			else:
				prev = n
                        	n = n.link
		if found != 1:
			return "Node Not Found"
		else:
			if n.link == None:
				prev.link = None
			else:
	                	next = n.link
				n.info = next.info
				n.link = next.link	

l = [10,20,30,40,50,60,70,80]
ll = LinkedList()
for i in l:
        ll.insert(i)
print ll

ll.delMiddleNode(30)
print ll

ll.delMiddleNode(10)
print ll

ll.delMiddleNode(50)
print ll

ll.delMiddleNode(80)
print ll
