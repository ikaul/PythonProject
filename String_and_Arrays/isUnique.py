#!/usr/bin/python
import unittest

#Check if string has all unique characters
def isUnique(str):
	if str == None:
		return None
	if len(str) < 2:
		return True
	strArr = list(str)
	if len(list(set(strArr))) == len(strArr):
		return True
	else:
		return False

class TestisUnique(unittest.TestCase):
	def setUp(self):
		self.str1 = "test"
		self.str2 = "ABCDEFGH"
		self.str3 = "AaBCDEFGHijklmpoqw"
	def test_validInput(self):
		self.assertFalse(isUnique(self.str1))
		self.assertTrue(isUnique(self.str2))
		self.assertTrue(isUnique(self.str3))
		self.assertTrue(isUnique(""))
		self.assertTrue(isUnique("A"))
		self.assertFalse(isUnique("AA"))
	def test_invalidInput(self):
		self.assertEqual(None, isUnique(None))

if __name__ == '__main__':
    unittest.main()
