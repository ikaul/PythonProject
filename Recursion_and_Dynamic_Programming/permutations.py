#!/usr/bin/python
"""
Given a string. list out all it's permutations.
"""

def permutations(s):
	if len(s) == 0:
		return [] 
	if len(s) == 1:
		return [s]
	l = []
	for i in range(len(s)):
		m = s[i]
		remList = s[:i] + s[i+1:]
		for p in permutations(remList):
			l.append([m]+p)
	return l
print permutations(list("ABC"))
