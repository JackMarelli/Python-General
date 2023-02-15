from gvars import *
from classes import Fruit

pygame.init()
pygame.display.set_caption("Fruit Ninja")

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.time.get_ticks() % (1000 / spawn_rate) == 0:
        new_fruit = Fruit()
        items.append(new_fruit)

    # Clear the screen
    screen.blit(background, (0, 0))

    # Update the fruits
    dt = clock.tick(60) / 1000
    for i in items:
        i.update(dt)
        screen.blit(i.image, i.rect)

    # Check for cursor collision with fruits
    cursor_pos = pygame.mouse.get_pos()
    for i in items:
        if i.rect.collidepoint(cursor_pos):
            print("fruit cut")
            items.remove(i)
            score += 1
        if i.rect.y > screen_height + fruit_size:
            print("fruit out of screen")
            items.remove(i)
            lives -= 1
            if lives <= 0 and not immortality:
                print("game over")
                running = False

    # remove fruits that are out of the screen

    # Update the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (screen_width - lives_text.get_width() - 10, 10))

    # Update the screen
    pygame.display.flip()
