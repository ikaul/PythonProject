#!/usr/bin/python
import unittest

class Solution(object):
	def __init__(self, matrix):
		self.matrix = matrix

	def moveRight(self, i, min, max, arr):
		for index in range(min, max+1):
			arr.append(self.matrix[i][index])
		
	def moveLeft(self, i, max, min, arr):
		for index in range(max - min + 1):
			arr.append(self.matrix[i][max - index])

	def moveDown(self, j, min, max, arr):
		for index in range(min, max+1):
			arr.append(self.matrix[index][j])
		
	def moveUp(self, j, max, min, arr):
		for index in range(max - min + 1):
			arr.append(self.matrix[max - index][j])

	def to_a(self):
		i = 0
		j = 0
		iMax = len(self.matrix)-1
		jMax  = len(self.matrix[0])-1
		arr = list()

		for l in self.matrix:
			if len(l) - 1 != jMax:
				raise ValueError('All rows must have the same number of columns')
		
		while (1):
			if i <= iMax:
				self.moveRight(i, j, jMax, arr)
				i += 1
			else:
				break

			if j <= jMax:
				self.moveDown(jMax, i, iMax, arr)
				jMax -= 1
			else:
				break
			
			if i <= iMax:
				self.moveLeft(iMax, jMax, j, arr )
				iMax -= 1
			else:
				break

			if j <= jMax:
				self.moveUp(j, iMax, i, arr )
				j += 1
			else:
				break

		return arr


class Test_spiral(unittest.TestCase):
	def test_MxN_Array(self):
		arr = [
                                [1,  2,  3,  4],
                                [5,  6,  7,  8],
                                [9,  10, 11, 12],
                                [13, 14, 15, 16],
                                [17, 18, 19, 20]
                      ]
		A = Solution(arr)
		self.assertEqual([1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10], A.to_a())


	def test_1xN_Array(self):
		B = Solution([[1,2,3,4]])
		self.assertEqual([1,2,3,4], B.to_a())

	def test_Mx1_Array(self):
		C = Solution([['a'], ['b'], ['c'], ['d']])
		self.assertEqual(['a', 'b', 'c', 'd'], C.to_a())

	def test_MxM_Array(self):
		arr = [
                                [1,  2,  3,  4],
                                [5,  6,  7,  8],
                                [9,  10, 11, 12],
                                [13, 14, 15, 16],
                      ]
		D = Solution(arr)
		self.assertEqual([1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10], D.to_a())
		
	def test_UnEqualColumns(self):
		arr = [
                                [1,  2,  3,  4],
                                [5,  6,  7,  8],
                                [9,  10, 11],
                                [13, 14, 15, 16],
                      ]
		E = Solution(arr)
		try:
			E.to_a()
			assert False
		except ValueError:
			assert True

	def test_1x0_Array(self):
		F = Solution([[1]])
		self.assertEqual([1], F.to_a())
unittest.main()
