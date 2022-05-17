class Snake:

    def __init__(self, initial_positions, direction, max_speed, speed_increment):
        self.snake = initial_positions
        self.direction = direction
        self.max_speed = max_speed
        self.speed_increment = speed_increment
        self.moved = True

        self.move_snake_head = {
            "right": lambda: (self.snake[0][0] + 1, self.snake[0][1]),
            "left": lambda: (self.snake[0][0] - 1, self.snake[0][1]),
            "up": lambda: (self.snake[0][0], self.snake[0][1] - 1),
            "down": lambda: (self.snake[0][0], self.snake[0][1] + 1)
        }

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_moved_false(self):
        self.moved = False

    def snake_update(self):
        for i in range(len(self.snake) - 1):
            self.snake[-(i + 1)] = self.snake[-(i + 2)]

    def snake_head_move(self, direction):
        self.snake[0] = self.move_snake_head[direction]()
        self.moved = True
