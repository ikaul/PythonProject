#!/usr/bin/python
from enum import Enum
from random import shuffle

class Suit(Enum):
	Club = 0
	Diamond = 1
	Heart = 2
	Spade = 3

class Card(object):
	suitValue = ["Club", "Diamond", "Heart", "Spade"]
	faceValues = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
	def __init__(self, value, suit, faceValue):
		self.value = value
		self.suit = suit
		self.faceValue = faceValue 

	def __str__(self):
		return str(self.faceValue) + " | " + self.suitValue[self.suit] + " | " + str(self.value)	

class Deck(Card):
	def __init__(self, type):
		self.cards = list()
		if type == "BlackJack":
			for suit in range(4):
				for card in range(13):
					if card == 0:
						value = 1
					elif card > 9:
						value = 10
					else:
						value = card + 1
					self.cards.append(Card(value, suit, Card.faceValues[card]))
		elif type == "Poker":
			self.cards = [Card(card, suit, Card.faceValues[card]) for suit in range(4) for card in range(13)]
				
			

	def __str__(self):
		ret = ""
		for card in self.cards:
			ret += str(card) + "\n"
		return ret

	def shuffle(self):
		shuffle(self.cards)
		return "Cards Shuffled"

	def takeOne(self):
		card = self.cards.pop(0)
		print card
		return card

class Hand(Card):
	def __init__(self):
		self.cards = list()

	def addCard(self, card):
		self.cards.append(card)

	def score(self):
		score = 0
		for card in self.cards:
			score += card.value
		return score

class BlackJackHand(Hand):
	def __init__(self):
		Hand.__init__(self)

	def score(self):
		score = 0
		A_count = 0
		for card in self.cards:
			if card.faceValue == "A":
				A_count += 1
			else:
				score += card.value
			score += A_count
			while A_count:
				if score < 21:
					score += 10
				A_count -= 1
				
		return score

d = Deck("BlackJack")
d.shuffle()
h = BlackJackHand()
while h.score() < 16:
	h.addCard(d.takeOne())
if h.score() > 21:
	print "Busted!!"
elif h.score() == 21:
	print "You Win!"
else:
	print "You might Win"
