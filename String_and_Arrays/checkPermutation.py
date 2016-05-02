#!/usr/bin/python
#Given 2 str, check if they are permutaion of each other
def checkPermutation(str1,str2):
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

print checkPermutation("test", "etst")
print checkPermutation("best", "etst")
print checkPermutation("ta", "at")
print checkPermutation("bbbbbbbeeeeeestt", "etstbbbbbbbeeeee")
