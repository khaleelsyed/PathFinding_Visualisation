import pygame

# pygame constants
WINDOW_WIDTH = 800  # Pixels
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))  # Window will be a square
pygame.display.set_caption('A* Pathfinding Visualisation')

ROWS = 25

# Colour space
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)


class Node:
    def __init__(self, row, col, width, total_rows):
        """

        :param row: Row that the node is located
        :param col: Column that the node is located
        :param width: Row Width
        :param total_rows: The number of rows in the grid
        """
        self.row = row
        self.col = col
        self.colour = WHITE
        self.width = width
        self.total_rows = total_rows

        self.x = self.col * self.width
        self.y = self.row * self.width
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

    def draw(self, surface):
        """
        Draws the cell representing the node on the grid on the display

        :param surface: Display Surface of pygame window
        """
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        """
        Adds all valid neighbouring nodes to a list

        :param grid: Grid representation as a nested list
        """
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
            # Bottom Node
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            # Top Node
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
            # Right Node
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            # Left Node
            self.neighbours.append(grid[self.row][self.col - 1])


def h(current_node, goal_node) -> int:
    """
    Heuristic Function for this algorithm: Manhattan Distance

    :param current_node: Current node being "explored"
    :param goal_node: Goal node for the algorithm
    :return: Manhattan distance between the two nodes on the grid
    """

    x1, y1 = current_node.get_pos()
    x2, y2 = goal_node.get_pos()

    return abs(y2 - y1) + abs(x2 - x1)


def algorithm(draw, grid, start_node, goal_node) -> bool:
    """
    A* Algorithm backbone

    :param draw: Draw function passed on with all arguments as a lambda
    :param grid: Grid representation
    :param start_node: Start (root) node for the search
    :param goal_node: Goal node for the search
    :returns : True if there is a successful path, False otherwise
    """
    pass  # TODO: Implement algorithm


def make_grid(rows, window_width):
    """
    Creates the data structure for the grid

    :param rows: The number of rows, the grid will contain
    :param window_width: The width (in pixels) of the display surface
    :return: A nested list representing the grid
    """
    row_width = window_width / rows
    grid = [[Node(i, j, row_width, rows) for j in range(rows)] for i in range(rows)]
    return grid


def draw_gridlines(surface, window_width, rows):
    """
    Draws the grid lines

    :param surface: Display surface
    :param window_width: The width of the display surface (pixels)
    :param rows: The number of rows in the grid
    """
    row_width = window_width / rows
    for i in range(rows):
        # Draw the horizontal lines
        pygame.draw.line(surface, GREY, (0, i * row_width), (window_width, i * row_width))
        for j in range(rows):
            # Draw the vertical lines
            pygame.draw.line(surface, GREY, (j * row_width, 0), (j * row_width, window_width))


def draw(surface, window_width, grid, rows):
    """
    Draws each node in the grid (of it's respective colour

    :param surface: Display surface
    :param window_width: Width of the display surface (in pixels)
    :param grid: The grid data type
    :param rows: The number of the rows in the grid
    """
    for row in grid:
        for node in row:
            node.draw(surface)

    draw_gridlines(surface, window_width, rows)
    pygame.display.update()


def convert_mouse_position(position, window_width, rows):
    """
    Converts the mouse position co-ordinates to rows and columns

    :param position: The co-ordinate of where the mouse was w.r.t. display surface
    :param window_width: The width of the display surface
    :param rows: The number of rows in the grid
    :return: Row and column in the grid
    """

    row_width = window_width // rows
    x, y = position  # (x, y)
    row = y // row_width
    col = x // row_width

    return row, col


def main(surface, window_width, rows):
    """
    Main function for the program

    :param surface:
    :param window_width:
    :param rows:
    """
    grid = make_grid(rows, window_width)

    start_node = None
    goal_node = None

    run = True

    while run:  # Starts the loop for pygame to be run
        draw(surface, window_width, grid, rows)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Primary Mouse Button
                mouse_position = pygame.mouse.get_pos()
                row, col = convert_mouse_position(mouse_position, window_width, rows)
                clicked_node = grid[row][col]

                if not start_node and clicked_node != goal_node:
                    start_node = clicked_node
                    start_node.make_start()

                elif not goal_node and clicked_node != start_node:
                    goal_node = clicked_node
                    goal_node.make_goal()

                elif clicked_node != start_node and clicked_node != goal_node:
                    clicked_node.make_wall()

            if pygame.mouse.get_pressed()[2]:  # Secondary Mouse Button
                mouse_position = pygame.mouse.get_pos()
                row, col = convert_mouse_position(mouse_position, window_width, rows)
                clicked_node = grid[row][col]
                clicked_node.reset()

                if clicked_node == start_node:
                    start_node = None

                elif clicked_node == goal_node:
                    goal_node = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and goal_node:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    algorithm(lambda: draw(surface, window_width, grid, rows), grid, start_node, goal_node)

                elif event.key == pygame.K_c:
                    start_node = None
                    goal_node = None
                    grid = None
                    grid = make_grid(rows, window_width)

    pygame.quit()


main(SURFACE, WINDOW_WIDTH, ROWS)
