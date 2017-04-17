#!/usr/bin/python
"""
Given a string s, find all its potential permutations. The output should be sorted in lexicographical order.

Example

For s = "CBA", the output should be
stringPermutations(s) = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"];
For s = "ABA", the output should be
stringPermutations(s) = ["AAB", "ABA", "BAA"].
Input/Output

[time limit] 4000ms (py)
[input] string s

A string containing only capital letters.

Guaranteed constraints:
1 <= s.length <= 5.

[output] array.string

All permutations of s, sorted in lexicographical order.
"""

def permutaions(start, end='', arr=[]):
    if len(start) == 0 and end not in arr:
        arr.append(end)
    else:
        for i in range(len(start)):
            permutaions(start[0:i] + start[i+1:], end + start[i], arr)
    return arr
        
def stringPermutations(s):
    return sorted(permutaions(s))
