#!/usr/bin/python
"""
Given a string that contains only digits 0-9 and a target value, return all expressions that are created by adding some binary operators (+, -, or *) between the digits so they evaluate to the target value. In some cases there may not be any binary operators that will create valid expressions, in which case the function should return an empty array. The numbers in the new expressions should not contain leading zeros.

The function should return all valid expressions that evaluate to target, sorted lexicographically.

Example

For digits = "123" and target = 6, the output should be
composeExpression(digits, target) = ["1*2*3", "1+2+3"].

Input/Output

[time limit] 4000ms (rb)
[input] string digits

Constraints:
2 <= digits.length <= 10.

[input] integer target

Constraints:
-104 <= target <= 104.

[output] array.string

"""

def composeExpression(digits, target):
	digitsArr = [int(x) for x in digits] #digits.chars.map { |i| i.to_i }
	digitsArr.sort()
	print digitsArr
	expressionArr = ['*', '/', '+', '-']
	sum = digitsArr[0]
	x = 0 
	i = 1 
	while ( sum <= int(target)):
		print "Index [" + str(i) + "] Sum = " + str(sum)
		if expressionArr[x] == '*':
        		sum = sum * digitsArr[i]
		elif expressionArr[x] == '+':
			sum = sum + digitsArr[i]
		elif expressionArr[x] == '-':
			sum = sum - digitsArr[i]
		elif expressionArr[x] == '/' and digitsArr[i] != 0:
			sum /= digitsArr[i]
		i += 1
		x += 1
composeExpression("435", "6")
