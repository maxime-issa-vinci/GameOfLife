class Cells:

    def __init__(self, v, h, SIZE_V, SIZE_H):
        self._value = 0
        self._will_live = False
        self._v = v
        self._h = h
        self._SIZE_V = SIZE_V
        self._SIZE_H = SIZE_H

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

    def is_alive(self):
        return self._value == 1

    def is_dead(self):
        return self._value == 0

    def live(self):
        self._value = 1

    def kill(self):
        self._value = 0

    def is_top_limit(self, a):
        return self._v == 0 and a == -1

    def is_right_limit(self, a):
        return self._h == self._SIZE_H - 1 and a == 1

    def is_left_limit(self, a):
        return self._h == 0 and a == -1

    def is_bottom_limit(self, a):
        return self._v == self._SIZE_V - 1 and a == 1

    def count_alive_neighbours(self, grid):
        count = 0
        for i in range(-1, 2):
            if self.is_top_limit(i):
                break
            elif self.is_bottom_limit(i):
                break

            for j in range(-1, 2):
                if self.is_left_limit(j):
                    break
                elif self.is_right_limit(j):
                    break
                elif grid[self._v + i][self._h + j] == 1:
                    count += 1
        return count

    def should_live_or_die(self, grid):
        count = self.count_alive_neighbours(grid)
        if count >= 3 and self.is_dead():
            self.live()
        elif count >= 2 and self.is_alive():
            self.live()
        elif (count < 2 or count > 3) and self.is_alive():
            self.kill()
        else:
            self.kill()

    def to_string(self):
        print(self._value, end=" ")
