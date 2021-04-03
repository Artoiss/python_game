import pygame
from pygame import Rect


class Button:

    # Add picture later
    def __init__(self, x, y, blockSize, blockWidth, text, window):
        self.position_x = x
        self.position_y = y
        self.blockSize = blockSize
        self.text = text
        self.blockWidth = blockWidth
        self.window = window
        self.draw_button()


    'Create "button" to the screen'
    def draw_button(self):
        myimage = pygame.image.load("./sprites/button_1.png")
        imagerect = Rect(self.position_x * self.blockSize,
                         self.position_y * self.blockSize,
                         self.blockSize,
                         self.blockSize
                         )

        self.window.blit(myimage, imagerect)

    'Remove button from the screen.'
    def remove_button(self):
        pygame.draw.rect(surface=self.window,
                         color=(110, 110, 110),
                         rect=Rect((self.position_x * self.blockSize),
                                   self.position_y * self.blockSize,
                                   self.blockSize * self.blockWidth,
                                   self.blockSize
                                   ))
