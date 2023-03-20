import pygame

pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define sprite dimensions
sprite_width = 50
sprite_height = 50

# Define a list of points for the sprite to follow
path_points = [(100, 100), (200, 300), (500, 200), (600, 400)]

# Create a sprite object
sprite = pygame.Surface((sprite_width, sprite_height))
sprite.fill((255, 0, 0))  # red color

# Define the starting point of the sprite
sprite_pos = pygame.math.Vector2(path_points[0])

# Set the initial target point for the sprite to move towards
target_point_index = 1
target_point = pygame.math.Vector2(path_points[target_point_index])

# Define the speed of the sprite
sprite_speed = 2

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite towards the target point
    direction = target_point - sprite_pos
    direction.normalize_ip()
    sprite_pos += direction * sprite_speed

    # Check if the sprite has reached the target point
    if (target_point - sprite_pos).length() < sprite_speed:
        target_point_index += 1
        if target_point_index == len(path_points):
            target_point_index = 0
        target_point = pygame.math.Vector2(path_points[target_point_index])

    # Draw the sprite on the screen
    screen.fill((255, 255, 255))  # white color
    screen.blit(sprite, (sprite_pos.x, sprite_pos.y))
    pygame.display.flip()

# Clean up
pygame.quit()
