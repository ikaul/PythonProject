#!/usr/bin/python


class Trie(object):
	def __init__(self):
		self.root = dict() 
	def _isValidWord(self, word):
		if not isinstance(word, basestring):
			print "Skipping since not valid word"
			return False
		return True

	def addWord(self, word):
		if not self._isValidWord(word):
			return False

		letters = list(word)
		current = self.root
		_end = '_end_'
		for letter in letters:
			current = current.setdefault(letter, {})
			#if not current.has_key(letter):
			#	current[letter] = {}
			#current = current[letter]

		current[_end] = _end

	def findWordInTrie(self, word):
		if not self._isValidWord(word):
			return False
		letters = list(word)
		current = self.root
		for x in letters:
			if current.has_key(x):
				print x
				current = current[x]
			else:
				return False
		return True


	def getWords(self, current, word):
		_end = '_end_'
		words = list()
		if current.keys() == None:
			word.append(word)
			return words
		for letter in current.keys():
			word = word + letter
			words.append(self.getWords(current[letter], word))
		

	def suggest(self, word):
		if not self._isValidWord(word):
			return None
		
		_end = '_end_'
		letters = list(word)
		suggestions = list()
		d_word = ""
		current = self.root
		for letter in letters:
			if current.has_key(letter):
				d_word += letter
			
			if current.has_key(_end):
				suggestions.append(d_word)
			current = current[letter]

		suggestions.append(self.getWords(current, word))
		return suggestions
		
t = Trie()
t.addWord("Hello")
t.addWord("World")
print t.root.items()
print t.findWordInTrie("World")
print t.suggest("Wor")
x = dict()
