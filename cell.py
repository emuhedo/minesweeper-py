#!/usr/bin/python

from random import randint

class Cell:
	def __init__(self,chance):
		if randint(0,99) < chance:
			self.isMine = True
		else:
			self.isMine = False
		self.covered = True
		self.cover = '#'

	def getIsMine(self):
		return self.isMine

	def getValue(self):
		return self.value

	def setValue(self,value):
		if value == '0':
			self.value = ' '
		else: 
			self.value = value
		return

	def isCovered(self):
		return self.covered

	def printCell(self):
		if self.covered:
			return self.cover
		else:
			return self.value

	def isSafe(self):
		if self.cover == 'F':
			return True
		else: 
			return False

	def uncover(self):
		self.covered = False
		return

	def toggleFlag(self):
		if self.cover == '#':
			self.cover = 'F'
		elif self.cover == 'F':
			self.cover = '#'