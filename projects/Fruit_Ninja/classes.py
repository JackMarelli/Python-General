import math
import pygame
import random

class Fruit:

    def __init__(self, x, y):
        self.fruit_images = ["assets/images/fruits/peach.png",
                        "assets/images/fruits/apple.png",
                        "assets/images/fruits/watermelon.png",
                        "assets/images/fruits/orange.png"]
        self.throw_angle = random.randint(-20, 20)
        self.x = x
        self.y = y
        self.image = pygame.image.load(random.choice(self.fruit_images))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = -random.randint(400, 500)
        self.acceleration = 420

    def update(self, dt):
        self.rect.y += self.velocity * dt
        self.rect.x += math.cos(self.throw_angle)
        self.velocity += self.acceleration * dt