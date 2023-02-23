import math
import random

import pygame

def point_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x < max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def point_inside_circle(point, circle):
    x, y = point
    center_x, center_y = circle[0], circle[1]
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    return distance <= circle[2]


# Initialize Pygame
pygame.init()

# Set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the caption
points = 0

# Set the player position and size
player_pos = [size[0] / 2, size[1] / 2]
player_size = [50, 50]

# Player and other object assets
player_color = (0, 0, 255)
player_speed = .25

obstacles = []
obstacles_color = (255, 0, 0)
obstacles_spawn_rate = 0.0007
obstacles_live_time = 3000  # ms

pickups = []
pickups_color = (0, 255, 0)
pickups_spawn_rate = 0.0004
pickups_live_time = 3000  # ms

obstacles_on = True
pickups_on = True

# Create a dictionary to store the keys that are pressed
keys = {
    'left': False,
    'right': False,
    'up': False,
    'down': False
}

# Run the game loop
running = True
while running:
    if points < 0:
        points = 0
    pygame.display.set_caption(str(points))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                keys['left'] = True
            elif event.key == pygame.K_d:
                keys['right'] = True
            elif event.key == pygame.K_w:
                keys['up'] = True
            elif event.key == pygame.K_s:
                keys['down'] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys['left'] = False
            elif event.key == pygame.K_d:
                keys['right'] = False
            elif event.key == pygame.K_w:
                keys['up'] = False
            elif event.key == pygame.K_s:
                keys['down'] = False

    # Move the player based on the keys that are pressed
    if keys['left']:
        player_pos[0] -= player_speed
    if keys['right']:
        player_pos[0] += player_speed
    if keys['up']:
        player_pos[1] -= player_speed
    if keys['down']:
        player_pos[1] += player_speed

    # Check if the player is out of bounds
    if player_pos[0] < 0 + player_size[0] / 2:
        player_pos[0] = 0 + player_size[0] / 2
    if player_pos[0] > size[0] - player_size[0] / 2:
        player_pos[0] = size[0] - player_size[0] / 2
    if player_pos[1] < 0 + player_size[1] / 2:
        player_pos[1] = 0 + player_size[1] / 2
    if player_pos[1] > size[1] - player_size[1] / 2:
        player_pos[1] = size[1] - player_size[1] / 2

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, player_color, (
        player_pos[0] - player_size[0] / 2, player_pos[1] - player_size[1] / 2, player_size[0], player_size[1]))

    # Generate obstacles
    if obstacles_on:
        if random.random() < obstacles_spawn_rate:
            # Get random point on the screen
            x = random.randint(0 + 25, size[0] - 25)
            y = random.randint(0 + 25, size[1])

            # Create a tuple with the triangle coordinates and the time it was spawned
            obstacle = ((x, y), (x + 25, y + 50), (x - 25, y + 50), pygame.time.get_ticks())

            # Add the triangle to the list
            obstacles.append(obstacle)

        # Iterate through the triangles list
        for obstacle in obstacles:
            # Draw the triangle
            pygame.draw.polygon(screen, obstacles_color, obstacle[:3])

        # Iterate through the triangles list
        for obstacle in obstacles:
            # Check if the triangle has been on the screen for more than 5 seconds
            if pygame.time.get_ticks() - obstacle[3] > obstacles_live_time:
                obstacles.remove(obstacle)
            if point_inside_polygon(player_pos, obstacle[:3]):
                obstacles.remove(obstacle)
                points -= 1

    # Generate pickups
    if pickups_on:
        if random.random() < pickups_spawn_rate:
            # Get random point on the screen
            x = random.randint(0 + 25, size[0] - 25)
            y = random.randint(0 + 25, size[1])

            # Create a tuple with the triangle coordinates and the time it was spawned
            pickup = (x, y, 25, pygame.time.get_ticks())

            # Add the triangle to the list
            pickups.append(pickup)

        for pickup in pickups:
            # Draw the triangle
            pygame.draw.circle(screen, pickups_color, (pickup[0], pickup[1]), 25)

        # Iterate through the triangles list
        for pickup in pickups:
            # Check if the triangle has been on the screen for more than 5 seconds
            if pygame.time.get_ticks() - pickup[3] > pickups_live_time:
                pickups.remove(pickup)
            if point_inside_circle(player_pos, pickup[:3]):
                pickups.remove(pickup)
                points += 1

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
