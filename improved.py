import math
from table import table


class Node:
    def __init__(self, position: tuple, distance: float, parent):
        self.__position = position
        self.__distance = distance
        self.__parent = parent

    def get_f(self, target):
        target_x, target_y = target
        current_x, current_y = self.__position
        h = math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)
        return self.__distance + h

    def get_distance(self):
        return self.__distance

    def get_pos(self):
        return self.__position

    def get_parent(self):
        return self.__parent


class ASTAR:
    def __init__(self, start, target, grid):
        self.__start = start
        self.__target = target
        self.__grid = grid

        self.__open = [Node(start, 0, None)]  # Nodes to be searched
        self.__closed = []  # Nodes which have been searched

        self.__current: Node | None = None

    def __select_closest(self):
        """STAGE 1: Selects the closest node to the end from the OPEN list"""
        closest = math.inf  # the f value of the closest node to the end
        current = None  # the node object of the current closest node to the end
        idx = 0  # the index in the OPEN list of the current closest node to the end
        for n, node in enumerate(self.__open):
            if node.get_f(self.__target) < closest:
                closest = node.get_f(self.__target)
                current = node
                idx = n
        del self.__open[idx]  # remove the selected node from OPEN list
        self.__closed.append(current)  # add the selected node to CLOSED list
        self.__current = current

    def __get_successors(self):
        """STAGE 2: acquires all adjacent nodes"""
        row, col = self.__current.get_pos()
        successors = []  # creating a list of successors which can be checked later

        distance = self.__current.get_distance() + math.sqrt(
            (row - self.__current.get_pos()[0]) ** 2 + (col - self.__current.get_pos()[1]) ** 2)
        if row - 1 > 0 and self.__grid[row][col] != 1:
            successors.append(Node((row - 1, col), distance, self.__current))
        if col - 1 > 0 and self.__grid[row][col] != 1:
            successors.append(Node((row, col - 1), distance, self.__current))
        if row + 1 > 0 and self.__grid[row][col] != 1:
            successors.append(Node((row + 1, col), distance, self.__current))
        if col + 1 > 0 and self.__grid[row][col] != 1:
            successors.append(Node((row, col + 1), distance, self.__current))
        return successors

    def __add_successors(self):
        """STAGE 3: checks if each acquired node needs to be added to OPEN or CLOSED list"""
        # discards the nodes which already have a better version in OPEN or CLOSED lists
        successors = self.__get_successors()
        t = self.__target
        for i, item in enumerate(self.__open):
            successors = [n for n in successors if n.get_pos() != item.get_pos() or n.get_f(t) < item.get_f(t)]
        for i, item in enumerate(self.__closed):
            successors = [n for n in successors if n.get_pos() != item.get_pos() or n.get_f(t) < item.get_f(t)]

        # removes all instances of the current node in the OPEN and CLOSED list and adds the node to the open list
        for s in successors:
            for o, opn in enumerate(self.__open):
                if opn.get_pos == s.get_pos():
                    del self.__open[o]
            for c, cls in enumerate(self.__closed):
                if cls.get_pos == s.get_pos():
                    del self.__closed[c]
            self.__open.append(s)

    def __backtrack(self):
        """STAGE 4: if a path is found, backtrack through every node to get there"""
        nodes = []
        node = self.__current
        while node:
            nodes.append(node.get_pos())
            node = node.get_parent()
        return nodes

    def run(self):
        while self.__open:  # loops until the OPEN list is empty, indicating there is no solution
            self.__select_closest()
            if self.__current.get_pos() == self.__target:
                return self.__backtrack(), [n.get_pos() for n in self.__closed]
            else:
                self.__add_successors()
        return None


if __name__ == "__main__":
    start = (0, 0)
    target = (88, 74)
    a = ASTAR(start, target, table)
    res = a.run()
    if res:
        print("path found")
        print(f"{len(res[1])} nodes checked")
    else:
        print("no path found")
    import pygame

    pygame.init()
    win = pygame.display.set_mode((1000, 1000))
    running = True

    while running:
        win.fill("white")
        for r, row in enumerate(table):
            for c, col in enumerate(row):
                if col == 1:
                    pygame.draw.rect(win, "black", (c * 10, r * 10, 10, 10))
        if res:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                for r in res[0]:
                    pygame.draw.rect(win, "red", (r[1] * 10, r[0] * 10, 10, 10))

        pygame.draw.rect(win, "green", (start[1] * 50, start[0] * 10, 10, 10))
        pygame.draw.rect(win, "green", (target[1] * 50, target[0] * 10, 10, 10))
        for r, row in enumerate(table):
            for c, col in enumerate(row):
                if col == 1:
                    pass

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
