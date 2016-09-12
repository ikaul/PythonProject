#!/usr/bin/python
def minSumArrayLen(s, nums):
	if not nums:
		return 0
		
	nums.sort(reverse=True)
	if s <= nums[0]:
		return 1	
	
	sum = nums[0]
	count = 1
	n = len(nums)
	index = 1
		
	while(index < n):
		sum += nums[index]
		if sum < s:
			index += 1
			count += 1
		else:
			return count + 1
	return 0

print minSumArrayLen(10, [1,4,5,5])
print minSumArrayLen(10, [])
print minSumArrayLen(100, [1,2,5,20])
print minSumArrayLen(4, [1,4,4])
