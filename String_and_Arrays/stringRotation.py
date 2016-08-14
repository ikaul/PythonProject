#!/usr/bin/python
import unittest

def stringRotation(str1, str2):
	if str1 == None and str2 == None:
		return True
	if str1 == None and str2 != None:
		return False
	if len(str1) == len(str2):
		s = str1 + str1
		if str2 in s:
			return True

	return False

class Test_stringRotation(unittest.TestCase):
	def setUp(self):
		self.str1 = "Hello World"
		self.str2 = "test"
		self.str3 = None
	def test_validInput(self):
		self.assertTrue(stringRotation(self.str1, "WorldHello "))
		self.assertTrue(stringRotation(self.str2, "stte"))
		self.assertFalse(stringRotation(self.str3, "test"))
		self.assertFalse(stringRotation(self.str1, "WorldHello"))

	def test_invalidInput(self):
		self.assertFalse(stringRotation(None, "test"))
		self.assertTrue(stringRotation(None, None))

unittest.main()
