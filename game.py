#!/usr/bin/python

try: 
    input = raw_input 
except NameError: 
    pass 

from field import Field

class Help:
	def setState(self,l):
		self.loop = l

	def printHelp(self):
		print("")
		print("Listed commands:")
		print(" try\t<x>\t<y>\tTests for mines")
		print(" flag\t<x>\t<y>\tPlaces flag")
		print(" ?\t<x>\t<y>\tPlaces questionmark")
		print(" restart\t\tStarts new game")
		print(" quit or exit\t\tQuits game")
		print(" help\t\t\tPrints list of commands")
		self.loop.command()

class Setup:
	def setState(self,l):
		self.loop = l

	def setup(self):
		print("")
		print("Select diffeculty:")
		print(" 1. Beginner\t\t(10 mines, 9x9)")
		print(" 2. Intermediate\t(40 mines, 16x16)")
		print(" 3. Expert\t\t(99 mines, 30x16)")
		print(" 4. Custom")
		print("")

		n = input("Choice: ")
		n = n.split()
		choice = int(n[0])

		if choice == 1:
			w = 9
			h = 9
			m = 10
		elif choice == 2:
			w = 16
			h = 16
			m = 40
		elif choice == 3:
			w = 30
			h = 16
			m = 99
		elif choice == 4:
			w = int(input("Width: "))
			h = int(input("Heigt: "))
			m = int(input("Mines: "))
		else:
			print(str(choice) + " is not a option.")
			self.setup()

		minefield = Field(w,h,m)
		self.loop.setMinefield(minefield)
		self.loop.command()

class Loop:
	def setStates(self,s,h,e):
		self.setup = s
		self.end = e
		self.help = h

	def setMinefield(self,m):
		self.minefield = m

	def command(self):
		self.minefield.printField()
		if(self.minefield.cleared()):
			self.end.endGame(False)

		command = input("Command >> ")
		c = command.split(' ')

		if c[0] == "try":
			if self.minefield.guess(ord(c[1])-65,int(c[2])-1):
				self.minefield.printField()
				self.end.endGame(True)
			self.command()
		elif c[0] == "flag":
			self.minefield.flag(ord(c[1])-65,int(c[2])-1)
			self.command()
		elif c[0] == "?":
			self.minefield.question(ord(c[1])-65,int(c[2])-1)
			self.command()
		elif c[0] == "restart":
			self.setup.setup()
		elif c[0] == "quit" or c[0] == "exit":
			exit()
		elif c[0] == "help":
			self.help.printHelp()
		else:
			print(c[0] + " is not a recognized command") 
			self.help.printHelp()

class End:
	def setState(self,s):
		self.setup = s

	def restart(self):
		choice = input("Do you want to start again? [y/n] ")
		choice = choice.split()
		choice = choice[0]
		if choice == "y":
			self.setup.setup()
		elif choice == "n":
			exit()
		else:
			print(str(choice) + " is not a valid choice")
			self.restart()

	def endGame(self,m):
		print("")
		if m:
			print("You hit a mine :o")
		else:
			print("You won :D")
		self.restart()