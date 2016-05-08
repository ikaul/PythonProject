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
	def isPalindrome(self):
		x = self.head
		y = self.head
		stack = list()
		while y != None and y.link != None:
			stack.append(x.info)
			x = x.link
			y = y.link.link
		if y != None:
			x = x.link
		while x != None:
			if x.info != stack.pop():
				return 0
			else:
				x = x.link
		return 1
				
		
list1 = list("Test") 
list2 = list("ABCDEDCBA") 
list3 = list("A") 
list4 = list("01ABA10") 
l1 = LinkedList()
l2 = LinkedList()
l3 = LinkedList()
l4 = LinkedList()
for i in list1:
        l1.insert(i)
for i in list2:
        l2.insert(i)
for i in list3:
        l3.insert(i)
for i in list4:
        l4.insert(i)

print l1.isPalindrome()
print l2.isPalindrome()
print l3.isPalindrome()
print l4.isPalindrome()
