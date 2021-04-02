import pygame
from unit import Unit
from building import Building
from map_grid import Map
import time

def main():
    # Initializations
    pygame.init()

    res_w = 720
    res_h = 480
    blockSize = 30

    window = pygame.display.set_mode((res_w, res_h))
    running = True

    # FPS setup for game loop
    FPS = 60
    clock = pygame.time.Clock()

    # Temporary base background
    window.fill((127, 127, 127))

    # Set basic map
    map_object = Map(window, blockSize, res_w, res_h)

    # Variable to help with recognizing single mouse event.
    mouse = 1

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # If mouse is released new click is possible.
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = 1

        # Get mouse position and information if mouse button is clicked.
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and mouse:
            # If map grid cell is empty, create building.
            if map_object.position_empty(pos) and map_object.object_selected == 0:
                map_object.create_building()

            else:
                map_object.select_building(pos)

            pygame.display.update()
            mouse = 0

        map_object.update_troops()

        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    main()

