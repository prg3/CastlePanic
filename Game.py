#!/usr/bin/python

from Board import Board
from Card import Card
from Monster import Monster

class Game:
	def __init__ (self,players):
		self.board = Board()
		self.cards = Card(players)
		self.monster = Monster()
		self.players = players
		cards = Card(self.players)

	def playTurn (self):
		self.drawUp()
		self.discardDraw()
		self.tradeCards()
		self.playCards()
		self.moveMonsters()
		self.drawMonsters()
		self.board.printBoard()
		self.isGameOver()

	def drawUp(self):
		print "Draw Phase"

	def discardDraw(self):
		print "Discard Phase"
		if players == 1:
			print "One Player"
			# Discard/Draw twice
		else:
			print "More than one player"
			# Just once

	def tradeCards(self,players):
		print "Trade Phase"
		if players == 6:
			print "Trade Twice"
			#Trade twice
		else:
			print "Just Once"
			#Just trade once

	def playCards(self):
		print "Play Cards"

	def moveMonsters(self):
		self.board.advanceMonster()

	def drawMonsters(self):
		print "Move Monsters Phase"

	def isGameOver(self):
		self.board.isGameOver()
