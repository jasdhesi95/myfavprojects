import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and size
snake_size = 20
snake_x = width / 2
snake_y = height / 2

# Snake movement variables
snake_x_change = 0
snake_y_change = 0

# Apple position
apple_size = 20
apple_x = round(random.randrange(0, width - apple_size) / 20) * 20
apple_y = round(random.randrange(0, height - apple_size) / 20) * 20

# Snake body
snake_body = []
snake_length = 1

# Game loop
running = True
clock = pygame.time.Clock()

def draw_snake():
    for part in snake_body:
        pygame.draw.rect(screen, green, [part[0], part[1], snake_size, snake_size])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check if snake has eaten the apple
    if snake_x == apple_x and snake_y == apple_y:
        apple_x = round(random.randrange(0, width - apple_size) / 20) * 20
        apple_y = round(random.randrange(0, height - apple_size) / 20) * 20
        snake_length += 1

    # Fill the screen with black color
    screen.fill(black)

    # Draw the apple
    pygame.draw.rect(screen, red, [apple_x, apple_y, apple_size, apple_size])

    # Update snake body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check if snake collides with its own body
    for part in snake_body[:-1]:
        if part == snake_head:
            running = False

    # Draw the snake
    draw_snake()

    # Update the display
    pygame.display.update()

    # Set the FPS
    clock.tick(10)

# Quit the game
pygame.quit()
