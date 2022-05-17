class Grid:

    def __init__(self, grid_size, cell_size, square_separation, screen_width, screen_height, black=(0, 0, 0)):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.square_separation = square_separation
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.grid = [[None] * grid_size for row in range(grid_size)]

        first_pixel_to_center_grid = (screen_width // 2 - (grid_size * (cell_size + square_separation) // 2),
                                      screen_height // 2 - (grid_size * (cell_size + square_separation) // 2))

        for i in range(0, grid_size):
            for j in range(0, grid_size):
                grid_dict = {
                    "colour": black,
                    "position_x": first_pixel_to_center_grid[0] + j * (cell_size + square_separation),
                    "position_y": first_pixel_to_center_grid[1] + i * (cell_size + square_separation)
                }
                self.grid[j][i] = grid_dict

    def change_cell_colour(self, cell, colour):
        # Let's think about applying some defensive programming here...
        # - Bounds checking against grid_size
        # - Individual functions for colour changes (reduce power of setters)

        self.grid[cell[0]][cell[1]]["colour"] = colour

    def get_cell_x_position(self, cell):

        return self.grid[cell[0]][cell[1]]["position_x"]

    def get_cell_y_position(self, cell):

        return self.grid[cell[0]][cell[1]]["position_y"]

    def get_colour(self, cell):

        return self.grid[cell[0]][cell[1]]["colour"]
