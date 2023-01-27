import random
import pygame
from pygame.locals import *
from classes import Fruit

pygame.init()
pygame.display.set_caption("Fruit Ninja")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
fruits = []
fruit_images = ["assets/images/fruits/peach.png",
                "assets/images/fruits/apple.png",
                "assets/images/fruits/watermelon.png",
                "assets/images/fruits/orange.png"]
score = 0
screen = pygame.display.set_mode((700, 500))

# add 10 random fruits to the list
for i in range(10):
    pos = (random.randint(50, 650), random.randint(50, 450))
    random_fruit = random.choice(fruit_images)
    fruits.append(Fruit(random_fruit, pos))

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the fruits
    dt = clock.tick(60) / 1000
    for fruit in fruits:
        fruit.update(dt)

    # Check for cursor collision with fruits
    cursor_pos = pygame.mouse.get_pos()
    for fruit in fruits:
        if fruit.rect.collidepoint(cursor_pos):
            fruits.remove(fruit)
            score += 1

    # Draw the fruits
    for fruit in fruits:
        screen.blit(fruit.image, fruit.rect)

    # Update the score
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()
