#!/usr/bin/python

def isPalindrome(s):
    strArr = list(s)
    n = len(s)
    i = 0
    
    print n
    for i in range(n/2):
	print i
        if strArr[i] != strArr[n-i-1]:
            return False
        
    return True

print isPalindrome("test")
print isPalindrome("abcba")
print isPalindrome("abba")
