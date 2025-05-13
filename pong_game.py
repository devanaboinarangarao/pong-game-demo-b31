import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)  # Color for paddles and ball
BLACK = (0, 0, 0)  # Background color

# Ball and paddle dimensions
BALL_RADIUS = 10  # Radius of the ball
PADDLE_WIDTH = 10  # Width of the paddles
PADDLE_HEIGHT = 100  # Height of the paddles

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball position and velocity
ball_x = WIDTH // 2  # Initial horizontal position of the ball
ball_y = HEIGHT // 2  # Initial vertical position of the ball
ball_dx = random.choice([-4, 4])  # Horizontal velocity of the ball
ball_dy = random.choice([-4, 4])  # Vertical velocity of the ball

# Paddle positions
left_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2  # Initial position of the left paddle
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2  # Initial position of the right paddle

# Paddle speed
paddle_speed = 5  # Speed at which paddles move

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user wants to quit
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Move left paddle
    if keys[pygame.K_w] and left_paddle_y > 0:  # Move up if 'W' is pressed
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:  # Move down if 'S' is pressed
        left_paddle_y += paddle_speed

    # Move right paddle
    if keys[pygame.K_UP] and right_paddle_y > 0:  # Move up if 'UP' arrow is pressed
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:  # Move down if 'DOWN' arrow is pressed
        right_paddle_y += paddle_speed

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:  # Reverse direction on collision
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or \
       (ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x < 0 or ball_x > WIDTH:  # Reset ball position if it goes out of bounds
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-4, 4])

    # Draw everything
    screen.fill(BLACK)  # Fill the screen with the background color
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Draw left paddle
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Draw right paddle
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)  # Draw the ball

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)  # Limit the game to 60 frames per second

pygame.quit()