#!/usr/bin/python
import unittest

def reverseNum(number):
	if not number:
		return None
	negative = 1
	if number < 0:
		number = number * -1
		negative = -1
	numArr = list(str(number))
	return  negative * int(''.join(numArr[::-1]))

class TestReverseNumber(unittest.TestCase):
	def setUp(self):
		self.n1 = 12345
		self.n2 = 10000
		self.n3 = 10101
		self.n4 = 110011
	def test_validInput(self):
		self.assertEqual(54321, reverseNum(self.n1))
		self.assertEqual(1, reverseNum(self.n2))
		self.assertEqual(self.n3, reverseNum(self.n3)) #Palindrome check

	def test_invalidInput(self):
		self.assertEqual(None, reverseNum(None))
		self.assertEqual(-1, reverseNum(-1000))
unittest.main()
