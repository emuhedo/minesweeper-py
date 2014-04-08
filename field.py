#!/usr/bin/python

from __future__ import print_function
from cell import Cell

class Field:
	def __init__(self,width,height,mines):	
		self.width = width
		self.height = height
		self.mines = mines
		self.createField()
		self.createHints()
		return

	def createField(self):		
		minesAdded = 0
		chance = (self.mines * 100) / (self.width * self.height)

		while minesAdded != self.mines:
			self.field = []
			minesAdded = 0
			for y in range(self.height):
				row = []
				for x in range(self.width):
					row.append(Cell(chance))
					if row[x].getIsMine():
						minesAdded += 1
				self.field.append(row)
		return 

	def createHints(self):
		for y in range(len(self.field)):
			for x in range(len(self.field[y])):
				cell = self.field[y][x]
				if cell.getIsMine():
					cell.setValue('x')
				else:
					m = str(self.getMinesAround(x,y))
					cell.setValue(m)
		return

	def getMinesAround(self,x,y):
		mines = 0
		for i in range(-1,2):
			for j in range(-1,2):
				xi = x+i
				yj = y+j
				if xi >= 0 and yj >= 0 and xi < self.width and yj < self.height:
					if self.field[yj][xi].getIsMine():
						mines += 1
		return mines

	def uncoverEmptyAround(self,x,y):
		for i in range(-1,2):
			for j in range(-1,2):
				xi = x+i
				yj = y+j
				if xi >= 0 and yj >= 0 and xi < self.width and yj < self.height:
					cell = self.field[yj][xi]
					if cell.isCovered():
						self.guess(xi,yj)
		return

	def printField(self):
		i = 1

		print("\n\t", end="")
		for char in range(0,self.width):
			print(chr(char+65) + " ", end="")
		print("\n")

		for list in self.field:
			print(str(i) + "\t", end = '')
			for item in list:
				print(item.printCell() + " ", end='')
			print("\t" + str(i))
			i += 1

		print("\n\t", end="")
		for char in range(0,self.width):
			print(chr(char+65) + " ", end="")
		print("\n")

	def cleared(self):
		safe = 0
		for y in range(len(self.field)):
			for x in range(len(self.field[y])):
				cell = self.field[y][x]
				if cell.getIsMine() and cell.isSafe(): 
					safe += 1

		if safe == self.mines:
			cleared = True
		else: 
			cleared = False

		return cleared



	def guess(self,x,y):
		cell = self.field[y][x]
		if cell.getValue() == " ":
			cell.uncover()
			self.uncoverEmptyAround(x,y)
			return False
		elif cell.getValue() == 'x':
			cell.uncover()
			return True
		else:
			cell.uncover()
			return False

	def flag(self,x,y):
		cell = self.field[y][x]
		cell.toggleFlag()