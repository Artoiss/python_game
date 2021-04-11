import pygame
from pygame import Rect
import math

class Unit:
    def __init__(self, pos, window, blockSize, gridmap, resource_object):
        self.blockSize = blockSize
        self.position_x = pos[0] * self.blockSize - 10
        self.position_y = pos[1] * self.blockSize - 10
        self.initial_pos_x = pos[0] * self.blockSize
        self.initial_pos_y = pos[1] * self.blockSize
        self.return_to_base = 0
        self.window = window
        self.gridmap = gridmap
        self.resource_object = resource_object
        self.target = self.get_resource_coordinates()
        self.init_time = 0
        self.create_troop()


    'Draws troop object to the map.'
    def create_troop(self):
        rect = Rect(self.position_x, self.position_y, 10, 10)
        pygame.draw.rect(self.window, (0, 0, 0), rect)


    'Calculate euclidian distance'
    def distance(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



    'Gets coordinates where nearest resource is located and returns it.'
    def get_resource_coordinates(self):
        min_dist = 10000
        min_x = []
        min_y = []
        for index_i, i  in enumerate(self.gridmap):
            for index_j, j in enumerate(i):
                if j == 'r':
                    # Calculate nearest resource with euclidian distance
                    dist = self.distance(index_i * self.blockSize, self.initial_pos_x, index_j * self.blockSize, self.initial_pos_y)
                    if dist < min_dist:
                        min_dist = dist
                        min_x = index_i
                        min_y = index_j
        return [min_x, min_y]

    'Calculates next position for the troop.'
    def calculate_next_position(self):
        # Coordinates in pixel system.
        pixel_coordinates = [i * self.blockSize for i in self.target]
        # If troop movement is towards resource.
        if (pixel_coordinates[0] != self.position_x or pixel_coordinates[1] != self.position_y) and self.return_to_base == 0:
            if pixel_coordinates[0] > self.position_x:
                self.position_x = self.position_x + 1

            elif pixel_coordinates[0] < self.position_x:
                self.position_x = self.position_x - 1

            if pixel_coordinates[1] > self.position_y:
                self.position_y = self.position_y + 1

            elif pixel_coordinates[1] < self.position_y:
                self.position_y = self.position_y - 1

        # If troop is at resource, set flag to return back to base.
        if (pixel_coordinates[0] == self.position_x and pixel_coordinates[1] == self.position_y):
            self.return_to_base = 1

        # If troop is at base, set flag to get back to resource.
        if (self.initial_pos_x == self.position_x and self.initial_pos_y == self.position_y):
            if self.return_to_base != 0:
                self.resource_object.add_wood()
            self.return_to_base = 0

        # If troop movement is back to base
        if self.return_to_base:
            if self.initial_pos_x > self.position_x:
                self.position_x = self.position_x + 1

            elif self.initial_pos_x < self.position_x:
                self.position_x = self.position_x - 1

            if self.initial_pos_y > self.position_y:
                self.position_y = self.position_y + 1

            elif self.initial_pos_y < self.position_y:
                self.position_y = self.position_y - 1


    'Moves the troop based on calculated next position.'
    def move(self):
        if self.init_time <= 5:
            self.calculate_next_position()

            myimage = pygame.image.load("./sprites/lumberjack_1_1.png")
            imagerect = Rect(self.position_x,
                                    self.position_y,
                                    self.blockSize,
                                    self.blockSize
                                    )

            self.window.blit(myimage, imagerect)

            self.init_time += 1
        elif self.init_time >= 5 and self.init_time <= 10:
            self.calculate_next_position()

            myimage = pygame.image.load("./sprites/lumberjack_1_2.png")
            imagerect = Rect(self.position_x,
                             self.position_y,
                             self.blockSize,
                             self.blockSize
                             )

            self.window.blit(myimage, imagerect)
            self.init_time += 1
            if self.init_time >= 10:
                self.init_time = 0




