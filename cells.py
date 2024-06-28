class Cells:

    def __init__(self, v, h, SIZE_V, SIZE_H):
        self._value = 0
        self._will_live = False
        self._v = v
        self._h = h
        self._SIZE_V = SIZE_V
        self._SIZE_H = SIZE_H

    def is_alive(self):
        return self._value==1

    def live(self):
        self._value = 1

    def kill(self):
        self._value = 0

    def count_alive_neighbours(self, grid):
        count = 0
        for i in range(-1, 2):

            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    vi = self._v + i
                    vh = self._h + j
                    if 0 <= vi < self._SIZE_V and 0 <= vh < self._SIZE_H:
                        if grid[vi][vh].is_alive():
                            count += 1
        return count

    def should_live_or_die(self, grid):
        count = self.count_alive_neighbours(grid)
        if self.is_alive():
            if count < 2 or count > 3:
                self._will_live = False
            else:
                self.will_live = True
        else:
            if count == 3:
                self._will_live = True
            else:
                self._will_live = False

    @property
    def will_live(self):
        return self._will_live

    @will_live.setter
    def will_live(self, value):
        self._will_live = value

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        self._v = value

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def to_string(self):
        print(self._value, end=" ")
