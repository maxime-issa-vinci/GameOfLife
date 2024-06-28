class Cells:

    def __init__(self, grid, v, h):
        self._value = 0
        self._will_live = False
        self._grid = grid
        self._v = v
        self._h = h

    @property
    def v(self):
        return self._v

    # Setter pour l'attribut age
    @v.setter
    def v(self, value):
        self._v = value

    @property
    def h(self):
        return self._h

    # Setter pour l'attribut age
    @h.setter
    def h(self, value):
        self._h = value

    def is_alive(self, v, h):
        return self._grid[v][h] == 1

    def is_dead(self, v, h):
        return self._grid[v][h] == 0

    def live(self, v, h):
        self._grid[v][h] = 1

    def kill(self, v, h):
        self._grid[v][h] = 0

    def is_top_limit(self, v, a):
        return v == 0 and a == -1

    def is_right_limit(self, h, a):
        return h == len(self._grid[0]) - 1 and a == 1

    def is_left_limit(self, h, a):
        return h == 0 and a == -1

    def is_bottom_limit(self, v, a):
        return v == len(self._grid) - 1 and a == 1

    def count_alive_neighbours(self, v, h):
        count = 0
        for i in range(-1, 2):
            if self.is_top_limit(v, i):
                break
            elif self.is_bottom_limit(v, i):
                break

            for j in range(-1, 2):
                if self.is_left_limit(h, j):
                    break
                elif self.is_right_limit(h, j):
                    break
                elif self._grid[v + i][h + j] == 1:
                    count += 1
        return count

    def should_live_or_die(self):
        count = self.count_alive_neighbours(self.v, self.h)

        if count >= 3 and self.is_dead(self.v, self.h):
            self.live(self.v, self.h)
        elif count >= 2 and self.is_alive(self.v, self.h):
            self.live(self.v, self.h)
        elif (count < 2 or count > 3) and self.is_alive(self.v, self.h):
            self.kill(self.v, self.h)
        else:
            self.kill(self.v, self.h)

    def to_string(self):
        print(self._value)
