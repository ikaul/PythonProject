#!/usr/bin/python
#Return permutaion of strings which are palindromes

def palindromePermutation(str):
	strArr = list(str)
	l = len(strArr)
	if l % 2 == 0 and getOddCharCount(str) == 0:
		return 1
	elif l % 2 == 1 and getOddCharCount(str) == 1:
		return 1
	else:
		return 0

def getOddCharCount(str):
	strArr = list(str)
	strCount = dict()
	for x in strArr:
		if strCount.has_key(x):
			strCount[x] += 1
		else:
			strCount[x] = 1
	count = 0
	for x in strCount.keys():
		if strCount[x] % 2 == 1:
			count += 1
	return count	
	return 1

print palindromePermutation("test")	
print palindromePermutation("e tet")	
print palindromePermutation("abcd abc")	
