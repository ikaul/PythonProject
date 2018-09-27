#!/usr/bin/python
"""
An array is called circular if we consider first element as next of last element. Circular arrays are used to implement queue (Refer this and this).

An example problem :
Suppose n people are sitting in a circular table with names A, B, C, D,.. Given a name, we need to print all n people (in order) starting from given name.
For example, consider 6 people A B C D E F and given name as D. People sitting in circular manner starting from D are D E F A B C.

A simple solution is to create an auxiliary array of size 2*n and store in another array. For example for 6 people, we create below auxiliary array.
A B C D E F A B C D E F
But this has O(N) space and O(N) time complexity.

We can do better.
O(N) time & O(1) Space Complexity Solution.
"""


class CircularArray(object):
    def __init__(self, list_of_items=[]):
        self.arr = list_of_items
        self.size = len(list_of_items)

    def _printFromIndex(self, index):
        """
        Prints the array from the index given in a cirtular manner
        Args:
                index: Integer - Start Index of Circular Array
        Returns:
                String: Iteration of Circular Array.
        """
        ret = str(self.arr[index])
        iterator = index + 1
        while iterator != index:
            ret += ' {}'.format(self.arr[iterator])
            iterator = iterator + 1
            iterator = iterator % self.size
        return ret

    def printCircularArray(self, letter):
        """
        Finds the element in the array to start from
        and prints array in circular fasion.
        Args:
                letter: value of element to start from.
        Returns:
                String: Iteration of Circular Array.
        """
        if letter in self.arr:
            index = self.arr.index(letter)
            return self._printFromIndex(index)
        else:
            return "Invalid Input"

import unittest
class TestCircularArray( unittest.TestCase ):
    def setUp(self):
        self.c_array = CircularArray(['A', 'B', 'C', 'D', 'E', 'F'])
        self.i_array = CircularArray([x for x in range(200)])
    def test_validInput(self):
        self.assertEqual(self.c_array.printCircularArray('D'), 'D E F A B C')
	self.assertEqual(self.c_array.printCircularArray('G'), 'Invalid Input')
	ret = [x + 100 for x in range(100)]
	ret.extend([x for x in range(100)])
	self.assertEqual(self.i_array.printCircularArray(100), ' '.join(map(str, ret)))

unittest.main()
