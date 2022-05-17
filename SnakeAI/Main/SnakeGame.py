import sys
import random
import pygame
from Grid import Grid
from Snake import Snake

# Comment
pygame.init()
size = width, height = 500, 500
black = (0, 0, 0)
white = (150, 150, 150)
green = (0, 255, 0)
screen = pygame.display.set_mode(size)
grid_size = 30
cell_size = 15
square_separation = 0
grid = Grid(grid_size, cell_size, square_separation, width, height)
snake = Snake([(15, 15), (14, 15), (13, 15)], "right", 150, 10)
red = (255, 0, 0)
speed = 0
moved = True

out_of_bounds = {
    "right": lambda: snake.snake[0][0] == grid.grid_size - 1,
    "left": lambda: snake.snake[0][0] == 0,
    "up": lambda: snake.snake[0][1] == 0,
    "down": lambda: snake.snake[0][1] == grid.grid_size - 1
}

turn_back_check = {
    pygame.K_LEFT: lambda: snake.get_direction() != "right",
    pygame.K_RIGHT: lambda: snake.get_direction() != "left",
    pygame.K_UP: lambda: snake.get_direction() != "down",
    pygame.K_DOWN: lambda: snake.get_direction() != "up",
}

input_keys = {
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}


def main():
    global speed
    spawn_food()
    while True:
        screen.fill(white)

        direction = snake.get_direction()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if turn_back_check[event.key] and snake.moved:
                    snake.set_moved_false()
                    snake.set_direction(input_keys[event.key])
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        snake.snake_update()
        if not out_of_bounds[direction]():
            snake.snake_head_move(direction)
        else:
            pygame.quit()
            sys.exit()
        if len(set(snake.snake)) != len(snake.snake):
            pygame.quit()
            sys.exit()
        check_for_food()

        for row in grid.grid:
            for cell in row:
                pygame.draw.rect(screen, cell["colour"],
                                 pygame.Rect(cell["position_x"], cell["position_y"],
                                             grid.cell_size, grid.cell_size))

        for body_section in snake.snake:
            pygame.draw.rect(screen, green, pygame.Rect(grid.get_cell_x_position(body_section),
                                                        grid.get_cell_y_position(body_section),
                                                        grid.cell_size, grid.cell_size))
        pygame.display.update()
        pygame.time.wait(200 - speed)


def check_for_food():
    global speed
    if grid.get_colour(snake.snake[0]) == red:
        grid.change_cell_colour(snake.snake[0], black)
        snake.snake.append(snake.snake[0])
        spawn_food()
        if speed < snake.max_speed:
            speed += snake.speed_increment


def spawn_food():
    grid.change_cell_colour((random.randint(0, grid.grid_size - 1), random.randint(0, grid.grid_size - 1)), red)


if __name__ == "__main__":
    main()
