import pygame
import random
import sys
import math


class Node:
    def __init__(self, target, parent):
        self.target = target
        self.parent = parent


class ASTAR:
    def __init__(self, grid):
        self.grid = grid

        self.start = 1, 1
        self.end = 10, 10

        self.open = [self.start]
        self.closed = []
3

class Graphic:
    def __init__(self):
        self.display_size = 20
        self.cell_size = 50
        self.distribution = 10
        self.size = (self.display_size*self.cell_size, self.display_size*self.cell_size)
        self.display = self.__setup()
        self.obstacles = self.__create_obstacles()

    def __setup(self):
        pygame.init()
        win = pygame.display.set_mode(self.size)
        return win

    def __create_obstacles(self):
        default = [[0 for _ in range(self.display_size)] for _ in range(self.display_size)]
        for r, row in enumerate(default):
            for c in range(len(row)):
                if random.randint(1, self.distribution) == 1 and (r, c) != (1, 1) and (r, c) != (10, 10):
                    default[r][c] = 1
        return default

    def __display(self):
        for r, row in enumerate(self.obstacles):
            for c, col in enumerate(row):
                if col == 1:
                    rect_arg = (c*self.cell_size, r*self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.display, "black", rect_arg)

        pygame.draw.rect(self.display, "red", (self.cell_size, self.cell_size, self.cell_size, self.cell_size))
        pygame.draw.rect(self.display, "blue", (self.cell_size*10, self.cell_size*10, self.cell_size, self.cell_size))

    def graphical(self):
        while True:
            self.display.fill("white")
            self.__display()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


main = Graphic()
main.graphical()
