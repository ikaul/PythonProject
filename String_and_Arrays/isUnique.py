#!/usr/bin/python
#Check if string has all unique characters
def isUnique(str):
	if len(str) < 2:
		return 1
	strArr = list(str)
	if len(list(set(strArr))) == len(strArr):
		return 1
	else:
		return 0

print isUnique("test")
print isUnique("ABCDEFGH")
print isUnique("")
print isUnique("AaBCDEFGHijklmpoqw")
