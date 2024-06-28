from cells import Cells

SIZE_H = 10
SIZE_V = 10

grid = [[0] * SIZE_H for i in range(SIZE_V)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        Cells(grid, i, j)


def main():
    for v in range(len(grid)):
        for h in range(len(grid[0])):
            Cells(grid, v, h).to_string()
            Cells(grid, v, h).should_live_or_die()
        print("\n")


if __name__ == "__main__":
    grid[1][1] = 1
    grid[1][2] = 1
    grid[1][3] = 1

    for i in range(3):
        main()
        print("------------------------")
