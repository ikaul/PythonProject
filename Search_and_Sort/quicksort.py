#!/usr/bin/python
import unittest
from random import randint
def quick_sort(arrayList, left=0, right=None):
	if arrayList is None:
		return None
	lenArray = len(arrayList)
	if right == None:
		right = lenArray - 1
	if left >= right:
		return arrayList
	
	#Randomize pivot element	
	pivot = randint(left, right)
	temp = arrayList[pivot]
	arrayList[pivot] = arrayList[right]
	arrayList[right] = temp
	pivot = right

	q = partition(arrayList, left, right-1, pivot)
	quick_sort(arrayList, left, q-1)
	quick_sort(arrayList, q+1, right)
	return arrayList

def partition(arrayList, left, right, pivot):
	lenArray = len(arrayList)
	while(1):
		while arrayList[left] < arrayList[pivot]:
			left = left + 1
		
		while arrayList[right] >= arrayList[pivot] and right > 0:
			right = right - 1

		if left >= right:
			temp = arrayList[left]
			arrayList[left] = arrayList[pivot]
			arrayList[pivot] = temp
			break
		else:
			temp = arrayList[left]
			arrayList[left] = arrayList[right]
			arrayList[right] = temp
	return left

class Test_Sort(unittest.TestCase):
	def setUp(self):
		self.list1 = [randint(1, 100) for x in range(100)]
		self.list2 = [randint(1, 100) for x in range(1000)]
	def test_validInput(self):
		self.assertEqual(sorted(self.list1), quick_sort(self.list1))
		self.assertEqual(sorted(self.list2), quick_sort(self.list2))
	def test_invalidInput(self):
		self.assertEqual([], quick_sort([]))
		self.assertEqual(None, quick_sort(None))

unittest.main()
