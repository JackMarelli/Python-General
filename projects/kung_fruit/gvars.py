import pygame, random, math, time, csv
from datetime import date
from utils import *

pygame.init()

# screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 20)
fruit_size = screen_height / 7
background = pygame.transform.scale(load_image("assets/images/background00.jpg"), (screen_width, screen_height))

allowed_spawn_screen_x_percent = 60
allowed_spawn_screen_x_pixels = screen_width / 100 * allowed_spawn_screen_x_percent

white = (255, 255, 255)
black = (0, 0, 0)

default_bg_color = white
default_text_color = black

# game
status = "main_menu"
immortality = False
bonus_score_value = 5
malus_score_value = 10

# images
fruit_names = ("apple", "orange", "watermelon", "peach")
malus_names = ("classic_bomb", "purple_bomb")
bonus_names = ("slow_banana", "party_banana", "immortality_fruit")

item_images = {"apple": "assets/images/fruits/apple.png", "watermelon": "assets/images/fruits/watermelon.png",
               "peach": "assets/images/fruits/peach.png", "orange": "assets/images/fruits/orange.png", }
