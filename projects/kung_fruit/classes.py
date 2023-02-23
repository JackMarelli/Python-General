from gvars import *
from utils import *

pygame.init()


# UI DEDICATED CLASSES AND SUBCLASSES
class Menu:

    def __init__(self):
        # everywhere useful text
        self.title_text = font.render("Kung Fruit", True, default_text_color)

        # main-menu useful text
        self.play_text = font.render("P - Play", True, default_text_color)
        self.options_text = font.render("O - Options ", True, default_text_color)
        self.exit_text = font.render("E - Exit ", True, default_text_color)

        # confirm-menu useful text
        self.confirm_text = font.render("Quit? Your score won't be saved :(", True, default_text_color)
        self.yes_text = font.render("Y - Yes", True, default_text_color)
        self.no_text = font.render("N - No", True, default_text_color)

    def main_menu(self):
        running = True
        while running:
            screen.fill(default_bg_color)
            screen.blit(self.title_text,
                        (50,
                         50))
            screen.blit(self.play_text,
                        (50,
                         150))
            screen.blit(self.options_text,
                        (50,
                         180))
            screen.blit(self.exit_text,
                        (50,
                         210))
            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                return "playing"
            elif keys[pygame.K_o]:
                return "options"
            elif keys[pygame.K_e]:
                return "quit"

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        return "quit"  # if something weird happens close the game, this shouldn't happen

    def pause_menu(self):
        pass

    def options_menu(self):
        pass

    def game_over_menu(self):
        running = True
        while running:
            pass

    def confirm_menu(self):
        running = True
        while running:
            screen.fill(default_bg_color)
            screen.blit(self.confirm_text, (50, 50))
            screen.blit(self.no_text, (50, 150))
            screen.blit(self.yes_text, (50, 180))
            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                return True
            elif keys[pygame.K_n]:
                return False

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        return False


# GAME DEDICATED CLASSES AND SUBCLASSES
class Match:
    def __init__(self, game_mode="classic"):
        self.score = 0
        self.lives = 3
        self.difficulty = 1
        self.game_mode = game_mode
        self.fruits_spawn_rate = 0.04
        self.malus_spawn_rate = 0.0
        self.items = []
        self.clock = pygame.time.Clock()
        print("match initialized")

    def loop(self):
        running = True
        menu = Menu()
        print("match started")
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        conf = menu.confirm_menu()
                        if conf:
                            running = False
                    elif keys[pygame.K_p]:
                        print("match paused")
                        menu.pause_menu()

            if self.game_mode == "classic":
                if random.random() < self.fruits_spawn_rate:
                    new_fruit = Fruit()
                    self.items.append(new_fruit)

                # Clear the screen
                screen.blit(background, (0, 0))

                # Update the fruits
                dt = self.clock.tick(60) / 1000
                for i in self.items:
                    i.update(dt)
                    screen.blit(i.image, i.rect)

                # Check for cursor collision with fruits or fruits out of screen
                cursor_pos = pygame.mouse.get_pos()
                for i in self.items:
                    if i.rect.collidepoint(cursor_pos):
                        print("fruit cut")
                        self.items.remove(i)
                        self.score += 1
                    if i.rect.y > screen_height + fruit_size:
                        print("fruit out of screen")
                        self.items.remove(i)
                        self.lives -= 1
                        if self.lives <= 0 and not immortality:
                            print("game over")
                            running = False

                # Update the score
                score_text = font.render(f"Score: {self.score}", True, default_text_color)
                screen.blit(score_text, (10, 10))

                lives_text = font.render(f"Lives: {self.lives}", True, default_text_color)
                immortality_text = font.render("You're immortal, have fun!", True, default_text_color)
                if immortality:
                    screen.blit(immortality_text, (screen_width - immortality_text.get_width() - 10, 10))
                else:
                    screen.blit(lives_text, (screen_width - lives_text.get_width() - 10, 10))

            pygame.display.flip()
        return self.score


# ITEMS DEDICATED CLASSES AND SUBCLASSES
class Item:  # all items have gravity, rect, have to spawn and get updated every cycle

    def __init__(self, image, item_type="fruit"):
        self.item_type = item_type
        self.x = random.randint((screen_width / 2 - allowed_spawn_screen_x_pixels / 2),
                                (screen_width / 2 + allowed_spawn_screen_x_pixels / 2))
        self.y = screen_height + fruit_size  # always spawn right below the screen
        self.image = pygame.transform.scale(image, (fruit_size, fruit_size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.throw_angle = random.randint(-20, 20)
        self.velocity = -random.randint(380, 550)
        self.acceleration = 400

    def update(self, dt):
        self.rect.y += self.velocity * dt
        self.rect.x += math.cos(self.throw_angle)
        self.velocity += self.acceleration * dt
        # todo: fix fruits going un in the sky while game is paused or in confirm menu


class Fruit(Item):  # Item subclass: Fruits use only the images from "images"  that have fruit names

    def __init__(self):
        self.image = load_image(item_images[random.choice(fruit_names)])
        super().__init__(self.image, item_type="fruit")
