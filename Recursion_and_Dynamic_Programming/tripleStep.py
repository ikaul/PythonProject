#!/usr/bin/python
import unittest
import sys
def tripleStep(num_steps):
	step_list = [ -1 for x in range(0,num_steps+1) ]
	try:
		return tripleStep_recursive(num_steps, step_list)
	except RuntimeError, e:
		return str(e)

def tripleStep_recursive(num_steps, step_list):
	if num_steps < 0:
		return 0
	elif num_steps == 0:
		return 1
	elif step_list[num_steps] > -1:
		return step_list[num_steps]
	else:
		step_list[num_steps] = tripleStep_recursive(num_steps-1, step_list) + tripleStep_recursive(num_steps-2, step_list) + tripleStep_recursive(num_steps-3, step_list)
		return step_list[num_steps]


class test_recursiveSteps(unittest.TestCase):
	def test_validInput(self):
		self.assertEqual(tripleStep(3), 4)
		self.assertEqual(tripleStep(50), 10562230626642)
	def test_boundary(self):
		self.assertEqual(tripleStep(1000), "maximum recursion depth exceeded")

unittest.main()
