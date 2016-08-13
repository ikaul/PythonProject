#!/usr/bin/python
#Replace repeated letters with letter counts
import unittest

def compress(input_str):
	if input_str == None:
		return None
	if len(input_str) <= 2:
		return input_str
	length = len(input_str)
	strArray = list(input_str)
	newArray = []
	count = 1 
	prev = strArray[0]
	for x in range(1, length):
		if prev == strArray[x]:
			count += 1
		else:
			if count > 2:
				newArray.append(str(count))	
				newArray.append(prev)
			else:
				for i in range(count):
					newArray.append(prev)
			count = 1
			prev = strArray[x]

	#For the last element
	if count > 2:
		newArray.append(str(count))
		newArray.append(prev)
	else:
		for i in range(count):
			newArray.append(prev)
	return ''.join(newArray)
	
class Test_compression(unittest.TestCase):
	def setUp(self):
		self.input_str1 = "aaaaAAAABBCC"
		self.input_str2 = "abcd"
		self.input_str3 = "space   compress"
		self.input_str4 = "aaAABBCC"
	def test_validInput(self):
		self.assertEqual("4a4ABBCC", compress(self.input_str1))
		self.assertEqual(self.input_str2, compress(self.input_str2))
		self.assertEqual("space3 compress", compress(self.input_str3))
		self.assertEqual(self.input_str4, compress(self.input_str4))

unittest.main()
