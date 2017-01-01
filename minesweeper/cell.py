from random import randint


class Cell:
    def __init__(self, chance):
        self._value = None

        if randint(0, 99) < chance:
            self.is_mine = True
        else:
            self.is_mine = False

        self.covered = True
        self.cover = '#'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value == 0:
            self._value = ' '
        else:
            self._value = str(value)

    @property
    def visible_value(self):
        if self.covered:
            return self.cover
        else:
            return self.value

    @property
    def safe(self):
        if self.cover == 'F':
            return True
        else:
            return False

    def uncover(self):
        self.covered = False

    def toggle_flag(self):
        if self.cover == '#':
            self.cover = 'F'
        elif self.cover == 'F':
            self.cover = '#'

#  vim: set ts=8 sw=4 tw=0 et :
