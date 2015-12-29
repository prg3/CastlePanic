#!/usr/bin/python

import json

class Monster:
	def __init__(self):	
		with open('monster.json') as data_file:    
			data = json.load(data_file)
