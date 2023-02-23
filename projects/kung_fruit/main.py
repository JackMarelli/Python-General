from classes import *

pygame.init()
pygame.display.set_caption("Kung Fruit")

running = True
status = "main_menu"
menu = Menu()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if status == "main_menu":
        status = menu.main_menu()
    elif status == "options":
        status = menu.options_menu()
    elif status == "playing":
        match = Match()
        latest_score = match.loop()
        status = "main_menu"
        print(f"latest score: {latest_score}")

    # Update the screen
    pygame.display.flip()
