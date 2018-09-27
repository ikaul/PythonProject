#!/usr/bin/python
"""
Sort s2 based on the char sequence of s1
for element not in s1, sort alphabatically
"""

def sortByString(s1, s2):
	h_s1 = {}
	index = 0
	for letter in list(s1):
		h_s1[letter] = { 'pos': index, 'count': 0 }
		index += 1

	ret = ''
	for letter in list(s2):
		if letter in h_s1:
			h_s1[letter]['count'] += 1
		else:
			ret += letter
	
	s2 = ''
	for letter in list(s1):
		num = h_s1.pop(letter)
		for _x in range(num['count']):
			s2 += letter

	return s2 + ret

s1 = "xabc"
s2 = "aaabacxxdefbbgchzxxxtx"
print sortByString(s1, s2)
