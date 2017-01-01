from minesweeper.cell import Cell


class Field:
    def __init__(self, width, height, nr_of_mines):
        self.width = width
        self.height = height

        self.create_field(nr_of_mines)
        self.create_hints()

    def create_field(self, nr_of_mines):
        mines_added = None
        chance = (nr_of_mines * 100) / (self.width * self.height)

        while mines_added != nr_of_mines:
            self.field = []
            mines_added = 0

            for _ in range(self.height):
                row = []
                for _ in range(self.width):
                    cell = Cell(chance)
                    row.append(cell)

                    if cell.is_mine:
                        mines_added += 1

                self.field.append(row)

    def create_hints(self):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell.is_mine:
                    cell.value = 'x'
                else:
                    cell.value = len(list(self.mines_around(x, y)))

    def cells_around(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                dx = x + i
                dy = y + j

                if dx >= 0 and dy >= 0 \
                        and dx < self.width and dy < self.height:
                    yield (dx, dy), self.field[dy][dx]

    def mines_around(self, x, y):
        for position, cell in self.cells_around(x, y):
            if cell.is_mine:
                yield cell

    @property
    def mines(self):
        for row in self.field:
            for cell in row:
                if cell.is_mine:
                    yield cell

    @property
    def covered_cells(self):
        for row in self.field:
            for cell in row:
                if cell.covered:
                    yield cell

    def uncover_empty_around(self, x, y):
        for position, cell in self.cells_around(x, y):
            if cell.covered:
                self.guess(*position)

    def print_column_names(self):
        print("\n\t", end="")

        for char in range(0, self.width):
            print(chr(char + 65) + " ", end="")

        print("\n")

    def print_row(self, count, row):
        print(str(count) + "\t", end='')

        for cell in row:
            print(cell.visible_value + " ", end='')

        print("\t" + str(count))

    def print(self):
        self.print_column_names()

        for count, row in enumerate(self.field):
            self.print_row(count + 1, row)

        self.print_column_names()

    @property
    def cleared(self):
        all_safe = True
        for mine in self.mines:
            all_safe &= mine.safe

        only_mines_covered = True
        for cell in self.covered_cells:
            only_mines_covered &= cell.is_mine

        return all_safe or only_mines_covered

    def guess(self, x, y):
        cell = self.field[y][x]
        if cell.value == " ":
            cell.uncover()
            self.uncover_empty_around(x, y)
            return False
        elif cell.value == 'x':
            cell.uncover()
            return True
        else:
            cell.uncover()
            return False

    def flag(self, x, y):
        cell = self.field[y][x]
        cell.toggle_flag()

#  vim: set ts=8 sw=4 tw=0 et :
