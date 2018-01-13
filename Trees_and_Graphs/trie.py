#!/usr/bin/python
#Trie Implementation in Python
class Trie(object):
    # Initialize Trie Data Structure
    def __init__(self):
        self.root = dict()
        self.end = '_end'
        self.count = '_count'
        self.word = '_word'

    # Add Word to Trie
    def add(self, word):
        wordArr = list(word)
        node = self.root
        for letter in wordArr:
            node = node.setdefault(letter, {})
            if self.count in node:
                node[self.count] += 1
            else:
                node[self.count] = 1
        node[self.end] = self.end
        node[self.word] = word

    # Suggest Words from Trie
    def word_suggestions(self, word):
        node = self.root
        for letter in list(word):
            if letter in node:
                node = node[letter]
            else:
                return []
        return self._word_suggestions(node)

    def _word_suggestions(self, node):
        words = list()
        if node == None:
            return []

        for key in node:
            if key == self.end:
                words.extend([node[self.word]])
            elif key != self.word and key != self.count:
                words.extend(self._word_suggestions(node[key]))
        return words

    # Show number of possible words that can be made from the given word
    def find(self, word):
        node = self.root
        for letter in list(word):
            if letter in node:
                node = node[letter]
            else:
                return 0
        return node[self.count]

words = ["Ishan", "Ishani", "IshanKaul", "IshKaul", "Test", "I_Test"]
trie = Trie()
for word in words:
    trie.add(word)

print trie.find("Ishan")
print trie.word_suggestions("Ish")
