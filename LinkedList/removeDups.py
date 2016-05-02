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

	def removeDuplicates(self):
		n = self.head
		prev = None
		hash = dict()
		hash[n.info] = 1
		while n.link != None:
			prev = n
			n = n.link
			if hash.has_key(n.info):
				prev.link = n.link
				n = prev
			else:
				hash[n.info] = 1

l = [10,20,30,10,20,30,10,20,40,50]
ll = LinkedList()
for i in l:
	ll.insert(i)
print ll

ll.removeDuplicates()
print ll

