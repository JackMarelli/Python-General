from gvars import *
from utils import *

class Item:

    def __init__(self, image, type="fruit"):
        self.type = type
        self.x = random.randint((screen_width/2-allowed_spawn_screen_x_pixels/2),(screen_width/2+allowed_spawn_screen_x_pixels/2))
        self.y = screen_height + fruit_size  # always spawn below the screen
        self.image = pygame.transform.scale(image, (fruit_size, fruit_size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.throw_angle = random.randint(-20, 20)
        self.velocity = -random.randint(380, 550)
        self.acceleration = 420

    def update(self, dt):
        self.rect.y += self.velocity * dt
        self.rect.x += math.cos(self.throw_angle)
        self.velocity += self.acceleration * dt

class Fruit(Item):

    def __init__(self):
        self.image = load_image(item_images[random.choice(fruit_names)])
        super().__init__(self.image)
