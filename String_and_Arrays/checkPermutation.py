#!/usr/bin/python
import unittest

#Given 2 str, check if they are permutaion of each other
def checkPermutation(str1,str2):
	if not isinstance(str1, str) or not isinstance(str2, str):
		return "Invalid Input"

	str1Arr = list(str1)
	str2Arr = list(str2)
	#They need to have same #chars
	if len(str1Arr) != len(str2Arr):
		return 0
	countHash = dict()
	for i in range(len(str1Arr)):
		if countHash.has_key(str1Arr[i]):
			countHash[str1Arr[i]] += 1
		else:
			countHash[str1Arr[i]] = 1 
		if countHash.has_key(str2Arr[i]):
			countHash[str2Arr[i]] -= 1
		else:
			countHash[str2Arr[i]] = -1
	
	for i in countHash.values():
		if i != 0:
			return 0 
	return 1 

class TestPermutations(unittest.TestCase):
	def test_validInput(self):
		self.assertTrue(checkPermutation("test", "etst"))
		self.assertFalse(checkPermutation("best", "etst"))
		self.assertTrue(checkPermutation("ta", "at"))
		self.assertTrue(checkPermutation("bbbbbbbeeeeeestt", "etstbbbbbbbeeeee"))
	def test_boundaryInput(self):
		self.assertTrue(checkPermutation("t", "t"))
		self.assertFalse(checkPermutation("x", "y"))
	def test_invalidInput(self):
		self.assertEqual(checkPermutation(-1, 1), "Invalid Input")
		self.assertEqual(checkPermutation(-1.0, 1), "Invalid Input")
		self.assertEqual(checkPermutation("test", 1), "Invalid Input")
		self.assertEqual(checkPermutation("test", None), "Invalid Input")
if __name__ == '__main__':
    unittest.main()
