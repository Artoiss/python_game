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

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #window.blit(image, image.get_rect(center = window.get_rect().center))
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:

            if map_object.position_empty(pos) and map_object.object_selected == 0:
                map_object.create_building()
            else:

                map_object.select_building(pos)

            pygame.display.update()
            time.sleep(0.3)

        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    main()

