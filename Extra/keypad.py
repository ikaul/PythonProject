#!/usr/bin/python

class Keypad(object):
	def __init__(self):
		self.keys = [x for x in range(10)]
		self.keys += ['*', '#', '<-']
		self.console = ""
		self.keypad = dict()

		ascii = 65
		self.keypad[0] = ['*']
		self.keypad[1] = ['~']
		keyID = 2
		while(ascii < 88):
			count = 3
			if keyID == 7 or keyID == 9:
				count = 4

			for i in range(count):
				if keyID not in self.keypad:
					self.keypad[keyID] = list()
				self.keypad[keyID].append(chr(ascii))
				ascii += 1
			keyID += 1	
			if chr(ascii) == 'z':
				break

	def __str__(self):
		return str(self.keys)
k = Keypad()
arr = [4,4,4,7,7,7,7,4,4,2,6,6]
