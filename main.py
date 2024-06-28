from cells import Cells

SIZE_H = 10
SIZE_V = 10

grid = [[Cells(i, j, SIZE_V, SIZE_H) for j in range(SIZE_H)] for i in range(SIZE_V)]


def main():
    for v in range(len(grid)):
        for h in range(len(grid[0])):
            grid[v][h].to_string()
            grid[v][h].should_live_or_die(grid)
        print("\n")


if __name__ == "__main__":
    grid[1][1].value = 1
    grid[1][2].value = 1
    grid[1][3].value = 1

    for i in range(2):
        main()
        print("------------------------")
