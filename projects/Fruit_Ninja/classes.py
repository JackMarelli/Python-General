import pygame


class Fruit:
    def __init__(self, image, pos, weight=1):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = pygame.math.Vector2(0, 0)
        self.weight = weight

    def update(self, dt):
        self.velocity += pygame.math.Vector2(0, 9.8) * self.weight * dt
        self.rect.move_ip(self.velocity)
def load_image(image_path):
    return pygame.image.load(image_path).convert_alpha()