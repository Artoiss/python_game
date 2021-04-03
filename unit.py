import pygame
from pygame import Rect

class Unit:
    def __init__(self, pos, window, blockSize, gridmap):
        self.blockSize = blockSize
        self.position_x = pos[0] * self.blockSize - 10
        self.position_y = pos[1] * self.blockSize - 10
        self.initial_pos_x = pos[0] * self.blockSize - 10
        self.initial_pos_y = pos[1] * self.blockSize - 10
        self.return_to_base = 0
        self.window = window
        self.gridmap = gridmap
        self.target = self.get_resource_coordinates()

        self.create_troop()

    def create_troop(self):
        rect = Rect(self.position_x, self.position_y, 10, 10)
        pygame.draw.rect(self.window, (0, 0, 0), rect)


    def get_resource_coordinates(self):
        for index_i, i  in enumerate(self.gridmap):
            for index_j, j in enumerate(i):
                if self.gridmap[index_i][index_j] == 'r':
                    return [index_i, index_j]


    def calculate_next_position(self):
        pixel_coordinates = [i * self.blockSize for i in self.target]
        if (pixel_coordinates[0] != self.position_x or pixel_coordinates[1] != self.position_y) and self.return_to_base == 0:
            if pixel_coordinates[0] > self.position_x:
                self.position_x = self.position_x + 1

            elif pixel_coordinates[0] < self.position_x:
                self.position_x = self.position_x + -1

            if pixel_coordinates[1] > self.position_y:
                self.position_y = self.position_y + 1

            elif pixel_coordinates[1] < self.position_y:
                self.position_y = self.position_y + -1

        if (pixel_coordinates[0] == self.position_x and pixel_coordinates[0] == self.position_y):
            self.return_to_base = 1

        if (self.initial_pos_x == self.position_x and self.initial_pos_y == self.position_y):
            self.return_to_base = 0

        if self.return_to_base:
            if self.initial_pos_x > self.position_x:
                self.position_x = self.position_x + 1

            elif self.initial_pos_x < self.position_x:
                self.position_x = self.position_x + -1

            if self.initial_pos_y > self.position_y:
                self.position_y = self.position_y + 1

            elif self.initial_pos_y < self.position_y:
                self.position_y = self.position_y + -1






    def move(self):
        self.calculate_next_position()

        #self.position_x = self.position_x - 1
        #self.position_y = self.position_y - 1


        rect = Rect(self.position_x - 1, self.position_y, 10, 10)
        pygame.draw.rect(self.window, (0, 0, 0), rect)



