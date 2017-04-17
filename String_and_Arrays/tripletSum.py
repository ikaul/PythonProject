#!/usr/bin/python
import unittest

"""Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.

Example

    For x = 15 and a = [14, 1, 2, 3, 8, 15, 3], the output should be
    tripletSum(x, a) = false;

    For x = 8 and a = [1, 1, 2, 5, 3], the output should be
    tripletSum(x, a) = true.

    The given array contains the elements 1,2, and 5, which add up to 8.

Input/Output

    [time limit] 4000ms (py)

    [input] integer x

    Guaranteed constraints:
    1 <= x <= 3000.

    [input] array.integer a

    Guaranteed constraints:
    3 <= a.length <= 1000,

    1 <= a[i] <= 1000.

    [output] boolean

    Return true if the array contains three elements that add up to x and false otherwise.

"""

def tripletSum(x, a):
    n = len(a)
    a = sorted(a)
            
    for i in range(n):
        num1 = a[i]
        start = i+1
        end = n-1
        
        while start < end:
            num2 = a[start]
            num3 = a[end]
            
            sum = num1 + num2 + num3 
            if sum == x:
                return True
            elif sum > x:
                end = end - 1
            elif sum < x:
                start = start + 1
    
    return False


class Test_TripletSum(unittest.TestCase):
	def test_validTest(self):
		self.assertTrue(tripletSum(8, [1, 1, 2, 5, 3]))
		self.assertFalse(tripletSum(15, [14, 1, 2, 3, 8, 15, 3]))

unittest.main()
