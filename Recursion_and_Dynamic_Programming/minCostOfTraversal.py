#!/usr/bin/python

class Solution():
	maxInt = 100000 
	def __init__(self, m, n):
		self.memo = list()
		for i in range(m):
			self.memo.append([self.maxInt for j in range(n)])
		
	def findMinCost(self, cost, m, n):
		if m == 0 and n == 0:
			return cost[m][n]
		elif m < 0 or n < 0:
			return self.maxInt
		elif self.memo[m][n] < self.maxInt:
			return self.memo[m][n]
		else:	
			self.memo[m][n] = cost[m][n] + min([self.findMinCost(cost, m-1, n-1), self.findMinCost(cost, m, n-1), self.findMinCost(cost, m-1, n)])
			return self.memo[m][n]

s = Solution(5,10)
cost = list()
for i in range(5):
	cost.append([j+1 for j in range(5)])

print s.findMinCost(cost, 4, 4)
