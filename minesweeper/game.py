from minesweeper.field import Field


class Help:
    def set_state(self, loop):
        self.loop = loop

    def print(self):
        print("""Listed commands:
 try    <x>    <y>    Tests for mines
 flag   <x>    <y>    Places flag
 restart              Starts new game
 quit or exit         Quits game
 help                 Prints list of commands
""")
        self.loop.command()


class Setup:
    def set_state(self, loop):
        self.loop = loop

    def setup(self):
        print("""Select diffeculty:
 1. Beginner        (10 mines, 9x9)
 2. Intermediate    (40 mines, 16x16)
 3. Expert          (99 mines, 30x16)
 4. Custom"
""")

        choice = int(
                input("Choice: ").split()[0])

        if choice == 1:
            width = 9
            height = 9
            mines = 10
        elif choice == 2:
            width = 16
            height = 16
            mines = 40
        elif choice == 3:
            width = 30
            height = 16
            mines = 99
        elif choice == 4:
            width = int(input("Width: "))
            height = int(input("Height: "))
            mines = int(input("Mines: "))
        else:
            print(str(choice) + " is not a option.")
            self.setup()

        minefield = Field(width, height, mines)
        self.loop.set_minefield(minefield)
        self.loop.command()


class Loop:
    def set_states(self, setup, help, end):
        self.setup = setup
        self.end = end
        self.help = help

    def set_minefield(self, minefield):
        self.minefield = minefield

    def command(self):
        self.minefield.print()
        if self.minefield.cleared:
            self.end.end_game(False)

        command = input("Command >> ").split(' ')

        if len(command) == 3:
            coordinate = (ord(command[1]) - 65, int(command[2]) - 1)

        if command[0] == "try":
            if self.minefield.guess(*coordinate):
                self.minefield.print()
                self.end.end_game(dead=True)
                return
            self.command()
        elif command[0] == "flag":
            self.minefield.flag(*coordinate)
            self.command()
        #  elif command[0] == "?":
        #      self.minefield.question(coordinate)
        #      self.command()
        elif command[0] == "restart":
            self.setup.setup()
        elif command[0] == "quit" or command[0] == "exit":
            exit()
        elif command[0] == "help":
            self.help.print()
        else:
            print(command[0] + " is not a recognized command")
            self.help.print()


class End:
    def set_state(self, setup):
        self.setup = setup

    def restart(self):
        choice = input("Do you want to start again? [y/n] ").split()[0]

        if choice == "y":
            self.setup.setup()
        elif choice == "n":
            exit()
        else:
            print(str(choice) + " is not a valid choice")
            self.restart()

    def end_game(self, dead):
        print("")

        if dead:
            print("You hit a mine :o")
        else:
            print("You won :D")

        self.restart()
