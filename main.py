import pygame
from unit import Unit
from building import Building
from map_grid import Map
from resources import Resources
import time
import os

def main():
    # Initializations
    pygame.init()

    res_w = 1080
    res_h = 900
    blockSize = 30
    sprite_list = load_images()
    window = pygame.display.set_mode((res_w, res_h))
    running = True

    # FPS setup for game loop
    FPS = 20
    clock = pygame.time.Clock()

    # Temporary base background
    window.fill((0, 110, 0))

    # Initialize players resources
    resource_object = Resources()

    # Set basic map
    map_object = Map(window, blockSize, res_w, res_h, sprite_list, resource_object)

    # Variable to help with recognizing single mouse event.
    mouse = 1

    # Game loop
    while running:
        map_object.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Esc for closing game.
        if event.type == 768:
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

            #pygame.display.update()
            mouse = 0

        map_object.update_troops()

        pygame.display.update()
        clock.tick(FPS)

'Load sprites from ./sprites'
def load_images():
    image_list = {}
    path = os.getcwd() + "/sprites"
    for sprite in os.listdir(path):
        image_path = path + "/" + sprite
        if image_path[-4:] == '.png':
            new_sprite = pygame.image.load(image_path)
            image_list[(sprite[:-4])] = new_sprite

    return image_list



if __name__ == "__main__":
    main()

