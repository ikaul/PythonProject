#!/usr/bin/python
import unittest

def groupsOfAnagrams(words):
    visited = {}
    for x in words:
        x_sorted = ''.join(sorted(x))
        if not visited.has_key(x_sorted):
            visited[x_sorted] = 1
    return len(visited.keys())

class UnitTest(unittest.TestCase):
	def test_validInput(self):
		self.assertEqual(groupsOfAnagrams(["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]), 4)
		self.assertEqual(groupsOfAnagrams(["tea"]), 1)
		self.assertEqual(groupsOfAnagrams(["tea", "eat", "eat", "ate","aet", "eta", "eat", "tae", "tea"]), 1)

unittest.main()
