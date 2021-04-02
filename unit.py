import pygame
from pygame import Rect

class Unit:
    def __init__(self, pos, window, blockSize):
        self.blockSize = blockSize
        self.position_x = pos[0] * self.blockSize - 10
        self.position_y = pos[1] * self.blockSize - 10
        self.window = window
        self.create_troop()

    def create_troop(self):
        rect = Rect(self.position_x, self.position_y, 10, 10)
        pygame.draw.rect(self.window, (0, 0, 0), rect)

    def move(self):
        #rect = Rect(self.position_x - 1, self.position_y, 10, 10)
        #pygame.draw.rect(self.window, (110, 110, 110), rect)

        self.position_x = self.position_x - 1
        self.position_y = self.position_y - 1

        rect = Rect(self.position_x - 1, self.position_y, 10, 10)
        pygame.draw.rect(self.window, (0, 0, 0), rect)



