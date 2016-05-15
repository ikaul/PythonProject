#!/usr/bin/python
import unittest

#Return permutaion of strings which are palindromes

def palindromePermutation(string):
	if not isinstance(string, str):
		return "Invalid Input"
	stringArr = list(string)
	l = len(stringArr)
	if l % 2 == 0 and getOddCharCount(string) == 0:
		return 1
	elif l % 2 == 1 and getOddCharCount(string) == 1:
		return 1
	else:
		return 0

def getOddCharCount(string):
	stringArr = list(string)
	stringCount = dict()
	for x in stringArr:
		if stringCount.has_key(x):
			stringCount[x] += 1
		else:
			stringCount[x] = 1
	count = 0
	for x in stringCount.keys():
		if stringCount[x] % 2 == 1:
			count += 1
	return count

class TestPalindromes( unittest.TestCase ):
	def test_validInput(self):
		self.assertFalse( palindromePermutation("test") )
		self.assertTrue( palindromePermutation("e tet") )
		self.assertFalse( palindromePermutation("abcd abc") )
	def test_boundaryInput(self):
		self.assertTrue( palindromePermutation("a") )
		self.assertTrue( palindromePermutation("") )
	def test_invalidInput(self):
		self.assertEqual( "Invalid Input", palindromePermutation(1) )
		self.assertEqual( "Invalid Input", palindromePermutation(None) )

unittest.main()
