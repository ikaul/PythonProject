#!/usr/bin/python

class Solution():
	maxInt = 100000 
	def __init__(self, m, n):
		self.minCost = list()
		for i in range(m):
			self.minCost.append([self.maxInt for j in range(n)])
	def findMinCost(self, cost, m, n):
		if m == 0 and n == 0:
			return cost[m][n]
		elif m < 0 or n < 0:
			return self.maxInt
		else:	
			return cost[m][n] + min([self.findMinCost(cost, m-1, n-1), self.findMinCost(cost, m, n-1), self.findMinCost(cost, m-1, n)])

		return self.minCost	

s = Solution(5,10)
cost = list()
for i in range(5):
	cost.append([j+1 for j in range(5)])
print cost
print s.findMinCost(cost, 4, 4)
