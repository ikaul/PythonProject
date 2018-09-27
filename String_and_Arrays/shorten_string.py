#!/usr/bin/python
from collections import defaultdict

def shorten_string(words):
	h_word = defaultdict(lambda: 0)
	word = list(words)
	for letter in word:
		h_word[letter] += 1
	ret = ""
	for letter in list(set(word)):
		ret += letter + str(h_word[letter])
	return ret


print shorten_string("TESTTTTTT")
