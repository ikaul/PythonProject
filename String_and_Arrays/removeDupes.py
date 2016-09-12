#!/usr/bin/python
import unittest

class RemoveDuplicates(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	if not nums:
		return 0
        nums.sort()
        index = 0
        for i in range(1, len(nums)):
            while(nums[i] <= nums[index]):
            	if i == len(nums)-1:
			print nums
                	return index+1
                i += 1
            index += 1
            nums[index] = nums[i]
            if i == len(nums)-1:
                return index+1

class Test_removeDuplicates(unittest.TestCase):
	def setUp(self):
		self.nums = [1,1,1,1,2,2,2,3,3] 
		self.nums_large = [x for x in range(-1000, 1000)]
		self.nums_short = [x for x in range(200)]
		self.dupes_nums = self.nums_large + self.nums_short
		self.emptyNums = []
		self.remDupes = RemoveDuplicates()
	def test_validInput(self):
		self.assertEqual(3, self.remDupes.removeDuplicates(self.nums))
		self.assertEqual(200, self.remDupes.removeDuplicates(self.nums_short))
		self.assertEqual(2000, self.remDupes.removeDuplicates(self.nums_large))
		self.assertEqual(2000, self.remDupes.removeDuplicates(self.dupes_nums))
		
	def test_invalidInput(self):
		self.assertEqual(0, self.remDupes.removeDuplicates(self.emptyNums))
		self.assertEqual(0, self.remDupes.removeDuplicates(None))

unittest.main()
