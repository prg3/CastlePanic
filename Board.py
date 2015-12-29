#!/usr/bin/python

class Board:
	def __init__(self):
		# Zone 5 is Forest
		# Zone 4 is Archer
		# Zone 3 is Knight
		# Zone 2 is Swordsman
		# Zone 1 is inside walls
		self.board = [
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1},
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1},
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1},
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1},
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1},
		{1:[],2:[],3:[],4:[],5:[],"Wall":1, "Reinforce":0,"Tower":1}
		]

	def printBoard( self ):
		board = self.board
		for section in board:
			if section["Reinforce"] == 1:
				wallStatus = "Reinforced"
			elif section["Wall"] == 1:
				wallStatus = "Standing"
			else:
				wallStatus = "Destroyed"

			if section["Tower"] == 1:
				towerStatus = "Standing"
			else:
				towerStatus = "Destroyed"

			print ("Forest : %s\tArcher : %s\tKnight : %s\tSwordman : %s\tWall : %s\t\tTower : %s\tInsideWalls : %s"%(section[5], section[4], section[3], section[2], wallStatus, towerStatus, section[1]))
		return

	def addMonster( self, monster, section):
		self.board[section][5].append(monster)
		return

	def advanceMonster( self ):
		skip = 0
		for zone in [1,2,3,4,5]:
			for sec in [5,4,3,2,1,0]:
				section = self.board[sec]
				if len(section[zone]) > 0:
					if zone == 1:
						if sec == 5 and skip == 0:
							self.board[0][zone] = section[zone]
							self.board[0]["Tower"] = 0
							section[zone] = []
							skip = 1
						elif sec < 5 and skip == 0:
							self.board[sec+1][zone] = section[zone]
							self.board[sec+1]["Tower"] = 0
							section[zone] = []

					elif zone == 2:
						if section["Wall"] == 1:
							if section["Reinforce"] == 1:
								section["Reinforce"] = 0
							else:	
								section["Wall"] = 0
						else:
							newzone = zone - 1 
							section[newzone] = section[zone]
							section[zone] = []
							section["Tower"] = 0
	
					else:
						newzone = zone - 1 
						section[newzone] = section[zone]
						section[zone] = []
		return

	def isGameOver( self ):
		over = 1
		for sec in [5,4,3,2,1,0]:
			if self.board[sec]["Tower"]:
				over = 0;
		return over

	def reinforceWall( self, section ):
		self.board[section]["Reinforce"] = 1
