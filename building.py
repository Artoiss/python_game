import pygame
from pygame import Rect
from button import Button
import time

'Class for creating building to the map.'
class Building:
    def __init__(self, pos, window, blockSize, res_w, res_h):
        self.window = window
        self.position = pos
        self.position_x = pos[0]
        self.position_y = pos[1]
        self.blockSize = blockSize
        self.res_w = res_w
        self.res_h = res_h
        self.draw_building()
        self.selected = 0

    'Returns position of the building '
    def get_position(self):
        return self.position

    'Draws building to the map'
    def draw_building(self):
        pygame.draw.rect(surface=self.window,
                         color=(90, 90, 90),
                         rect=Rect(self.position_x * self.blockSize + 1,
                                   self.position_y * self.blockSize + 1,
                                   self.blockSize -2,
                                   self.blockSize -2
                                   ))

    'Selects block and makes green square around it.'
    def select(self, status):
        # If we want to activate block.
        if status:
            col = [0, 150, 0]
            self.selected = 1

        # If we want to deactivate block.
        else:
            col = [110, 110, 110]
            self.selected = 0

        # Modify grid coordinates to pixel coordinates.
        x = self.position_x * self.blockSize
        y = self.position_y * self.blockSize

        # Draw square
        self.draw_line(x, y, x + self.blockSize, y, col)
        self.draw_line(x, y + self.blockSize, x, y, col)
        self.draw_line(x + self.blockSize, y, x + self.blockSize, y + self.blockSize, col)
        self.draw_line(x, y + self.blockSize, x + self.blockSize, y + self.blockSize, col)

    'Draws lines to GUI.'
    def draw_line(self, x1, y1, x2, y2, col):
        pygame.draw.lines(self.window, col, True,
                          [(x1, y1), (x2, y2)], 1)

