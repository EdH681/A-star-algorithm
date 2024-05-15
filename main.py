import math
import table
import pygame
import sys


class Node:
    def __init__(self, target, parent, distance, position):
        self.__parent = parent
        self.__target = target
        self.__distance_traveled = distance
        self.__position = position

    def get_parent(self):
        return self.__parent

    def get_position(self):
        return self.__position

    def get_distance(self):
        return self.__distance_traveled

    def get_f(self):
        target_x, target_y = self.__target
        current_x, current_y = self.__position
        h = math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)
        return self.__distance_traveled + h


class ASTAR:
    def __init__(self, grid):
        self.grid = grid

        self.start = 1, 1
        self.target = 3, 7

        self.open = [Node(self.target, None, 0, self.start)]
        self.closed = []

        self.current = None

    def __select_node(self):
        closest = math.inf
        current = None
        for i, node in enumerate(self.open):
            if node.get_f() < closest:
                current = node
                closest = node.get_f()
            del self.open[i]
            self.closed.append(current)
        return current

    def __generate_successors(self):
        row, column = self.current.get_position()
        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]):
                    if self.grid[r][c] != 1 and (r, c) != self.current.get_position():
                        node_distance = self.current.get_distance() + 1
                        successor = Node(self.target, self.current, node_distance, (r, c))
                        self.__add_successors(successor)

    def __add_successors(self, successor):
        for i, node in enumerate(self.open):
            if node.get_f() > successor.get_f():
                self.open[i] = successor
                break
        for i, node in enumerate(self.closed):
            if node.get_f() > successor.get_f():
                self.closed[i] = successor
                break
        self.open.append(successor)

    def __get_path(self):
        path = []
        ancestor = self.current
        while ancestor.get_parent():
            ancestor = ancestor.get_parent()
            path.append(ancestor.get_position())
        return path

    def run(self):
        repeat_check = []
        while self.open:
            self.current = self.__select_node()
            print(f"{self.current.get_position()}, {self.current.get_f()}")
            if self.current.get_position() == self.target:
                return self.__get_path()
            else:
                self.__generate_successors()
        print("no path")


grid = table.table
main = ASTAR(grid)
path = main.run()

pygame.init()
win = pygame.display.set_mode((900, 900))

running = True
while running:

    win.fill("white")

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 1:
                pygame.draw.rect(win, "black", (r*10, c*10, 10, 10))

    pygame.draw.rect(win, "blue", (10, 10, 10, 10))
    pygame.draw.rect(win, "green", (800, 600, 10, 10))

    #for i in range(len(path)-1):
    #    pygame.draw.line(win, "red", (path[i][0]*10+5, path[i][1]*10+5), (path[i+1][0]*100+50, path[i+1][1]*100+50), 10)

    for p in path:
        pygame.draw.rect(win, "red", (p[0]*10, p[1]*10, 10, 10))

        pygame.display.update()
        pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()