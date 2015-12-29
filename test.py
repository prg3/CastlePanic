#!/usr/bin/python

#from Board import Board

from Game import Game
thisGame = Game(3)

thisGame.cards.printHand(1)

#thisBoard = Board()

#print "Initial Conditions"
#thisBoard.addMonster(["Orc"], 4)
#thisBoard.reinforceWall(4)

#thisBoard.printBoard()

#for i in range(2,15):
#	print ""
#	print "Turn %s"%(i)
#	thisBoard.advanceMonster()
#	thisBoard.printBoard()
#	if thisBoard.isGameOver():
#		print "Game Over"
#		break
