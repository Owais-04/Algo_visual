

import pygame
import sys
from settings import *
from grid import make_grid, draw, get_clicked_pos
from algorithm import a_star_algorithm

pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorithm")

def main():
    grid = make_grid(ROWS, WIDTH)
    start = None
    end = None
    run = True

    while run:
        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:  # Left mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if not start:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    a_star_algorithm(lambda: draw(WIN, grid, ROWS, WIDTH), grid, start, end)

    pygame.quit()

if __name__ == "__main__":
    main()
