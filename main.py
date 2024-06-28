from cells import Cells
import pygame

SIZE_H, SIZE_V = 500, 250
WIDTH, HEIGHT = 1290, 720
grid = [[Cells(i, j, SIZE_V, SIZE_H) for j in range(SIZE_H)] for i in range(SIZE_V)]
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Line
grid[20][20].live()
grid[20][21].live()
grid[20][22].live()

# Pulsar
# Pulsar
grid[22][24].live()
grid[22][25].live()
grid[22][26].live()
grid[22][30].live()
grid[22][31].live()
grid[22][32].live()
grid[27][24].live()
grid[27][25].live()
grid[27][26].live()
grid[27][30].live()
grid[27][31].live()
grid[27][32].live()
grid[29][24].live()
grid[29][25].live()
grid[29][26].live()
grid[29][30].live()
grid[29][31].live()
grid[29][32].live()
grid[34][24].live()
grid[34][25].live()
grid[34][26].live()
grid[34][30].live()
grid[34][31].live()
grid[34][32].live()

grid[24][22].live()
grid[25][22].live()
grid[26][22].live()
grid[30][22].live()
grid[31][22].live()
grid[32][22].live()
grid[24][27].live()
grid[25][27].live()
grid[26][27].live()
grid[30][27].live()
grid[31][27].live()
grid[32][27].live()
grid[24][29].live()
grid[25][29].live()
grid[26][29].live()
grid[30][29].live()
grid[31][29].live()
grid[32][29].live()
grid[24][34].live()
grid[25][34].live()
grid[26][34].live()
grid[30][34].live()
grid[31][34].live()
grid[32][34].live()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray12")

    for v in range(len(grid)):
        for h in range(len(grid[0])):
            grid[v][h].should_live_or_die(grid)

    for v in range(len(grid)):
        for h in range(len(grid[0])):
            if grid[v][h].will_live:
                grid[v][h].live()
            else:
                grid[v][h].kill()

            if grid[v][h].is_alive():
                pygame.draw.rect(screen, "white", (100 + (h * 5), 100 + (v * 5), 5, 5))
            else:
                pygame.draw.rect(screen, "gray12", (100 + (h * 5), 100 + (v * 5), 5, 5))


    pygame.display.flip()

    clock.tick(1)

pygame.quit()
