#!/usr/bin/python

def singleNumber(nums):
    N = len(nums)
    if N % 2 == 0:
        return 0
    if N == 1:
        return nums[0]
        
    nums = sorted(nums)
    print nums
    index = 0
    while (index < N-1):
        if (nums[index] != nums[index + 1]):
	    print nums[index]
	    print nums[index + 1]
            return nums[index]
        index += 2
    return 0    

nums = [1,2,3,4,1,2,3]
print singleNumber(nums)
