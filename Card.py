#@/usr/bin/python

import json
import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Card:
	def __init__(self,players):
		with open('cards.json') as data_file:
			self.cards=json.load(data_file)
		self.cardDeck = []
	
		for i in range(0,players):
			self.cardDeck.append([])
			for j in range(0,self.cardsPerPlayer(players)-1):
				self.cardDeck[i].append(self.drawCard())

	def cardsPerPlayer(self,players):
		cpp = { 1:6, 2:6, 3:5, 4:5, 5:5, 6:4 }
		return cpp.get(players)

	def drawCard(self):
		availCards = []
		for card in self.cards:
			if card["inHand"] == False:
				if card["discard"] == False:
					availCards.append(card)
		card=random.choice(availCards)
		card["inHand"]=True
		return card

	def printHand(self,player):
		print "Printing Hand"
		for card in self.cardDeck[player]:
			print card["name"]
		
	def playCard(self):
		print "Pick a card to play"

	def showCards(self):
		print "Showing Cards"

	def playNormal(self):
		print "Playing a normal card"

	def NiceShot(self):
		print "Nice Shot"

	def Scavenge(self):
		print "Scavenge"

	def Fortify(self):
		print "Fortify"

	def Draw2(self):
		print "Draw 2 Cards"

	def Drive(self):
		print "Drive him back"

	def Missing(self):
		print "Missing"
