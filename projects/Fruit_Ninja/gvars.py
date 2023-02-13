import pygame, random, math, time
from utils import *

pygame.init()

# screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 20)
fruit_size = screen_height/7
background = pygame.transform.scale(load_image("assets/images/background00.jpg"), (screen_width, screen_height))
cursor_pos = pygame.mouse.get_pos()

allowed_spawn_screen_x_percent = 60
allowed_spawn_screen_x_pixels = screen_width / 100 * allowed_spawn_screen_x_percent

# game
status = "main_menu"
game_mode = "classic"
running = True
immortality = False
items = []
clock = pygame.time.Clock()
score = 0
lives = 3
spawn_rate = 40  # only dividers of 1000 todo: fix

# images
fruit_names = ("apple", "orange", "watermelon", "peach")
malus_names = ("classic_bomb", "purple_bomb")
bonus_names = ("slow_banana", "party_banana")

item_images = {"apple": "assets/images/fruits/apple.png", "watermelon": "assets/images/fruits/watermelon.png",
               "peach": "assets/images/fruits/peach.png", "orange": "assets/images/fruits/orange.png", }

