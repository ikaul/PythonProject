#!/usr/bin/python
#Replace String with %20
def urlify(str):
	strArr = str.split(" ")
	newStr = "%20".join(strArr) 
	return newStr

print urlify("test ing")
print urlify("test  ing")
print urlify("te st  ing")
print urlify("")
print urlify(" ")
