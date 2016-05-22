#!/usr/bin/python
import unittest
from random import randint

class SearchTest(unittest.TestCase):
	def setUp(self):
		self.arrayList = [ randint(1, 100) for x in range(10) ]
		self.arrayList = sorted(self.arrayList)
	def test_validInput(self):
		self.assertTrue(binary_search(self.arrayList, self.arrayList[2]))
		self.assertTrue(binary_search(self.arrayList, self.arrayList[8]))

	def test_invalidInput(self):
		self.assertFalse(binary_search(self.arrayList, -1))
		self.assertFalse(binary_search(self.arrayList, None))

	def test_boundaryInput(self):
		self.assertTrue(binary_search(self.arrayList, self.arrayList[9]))
		self.assertTrue(binary_search(self.arrayList, self.arrayList[0]))
		self.assertFalse(binary_search([], 9))
		self.assertTrue(binary_search([9], 9))

def binary_search(arrayList, testValue):
	lenArray = len(arrayList)
	if lenArray <= 0:
		return False
	if lenArray == 1:
		if arrayList[0] != testValue:
			return False
		else:
			return True

	if lenArray % 2 == 0:
		lenArray = int(lenArray / 2)
	else:
		lenArray = int(lenArray / 2) + 1

	if arrayList[lenArray] == testValue:
		return True
	elif arrayList[lenArray] > testValue:
		return binary_search(arrayList[:lenArray-1], testValue)
	elif arrayList[lenArray] < testValue:
		return binary_search(arrayList[lenArray+1:], testValue)		

unittest.main()
