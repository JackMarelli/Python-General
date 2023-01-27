import pygame

def load_image(image_path):
    return pygame.image.load(image_path).convert_alpha()