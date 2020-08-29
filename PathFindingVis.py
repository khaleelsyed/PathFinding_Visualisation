import pygame

# pygame constants
WIDTH = 800 # Pixels
SURFACE = pygame.display.set_mode((WIDTH, WIDTH)) # Window will be a square
pygame.display.set_caption('A* Pathfinding Visualtion')

# Colour space
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
ORANGE = (255, 128, 0)
YELLOW  = (255, 255, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.colour = WHITE
        self.width = width

        self.x = self.row * self.width
        self.y = self.col * self.width
        self.neighbours = []

    def get_pos(self):
        return self.x, self.y

    def is_wall(self) -> bool:
        return self.colour == BLACK

    def is_start(self) -> bool:
        return self.colour == RED

    def is_goal(self) -> bool:
        return self.colour == GREEN

    def is_open(self) -> bool:
        return self.colour == YELLOW

    def is_closed(self) -> bool:
        return self.colour == ORANGE

    def reset(self):
        self.colour = WHITE

    def make_wall(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = RED

    def make_goal(self):
        self.colour = GREEN

    def make_open(self):
        self.colour = YELLOW

    def make_closed(self):
        self.colour = ORANGE

    def make_path(self):
        self.colour = BLUE

    def draw(self):
        pass

    def update_neighbours(self):
        pass

def h(current_node, goal_node) -> int:
    """
    Heuristic Function for this algorith: Manhattan Distance

    :param current_node: Current node being "explored"
    :param goal_node: Goal node for the algorithm
    :return: Manhattan distance between the two nodes on the grid
    """

    x1, y1 = current_node.get_pos()
    x2, y2 = goal_node.get_pos()

    return abs(y2 - y1) + abs(x2 - x1)

def algorithm():
    """This method will contain the A* search algortihm backbone"""
    pass

def make_grid(rows, width):
    """This method will contain the grid mechanics"""
    pass

def main(surface, width):
    """This method will contain main loop for the program"""
    pass

main(SURFACE, WIDTH)