from pygame import Rect
import pygame
import math
from building import Building
from button import Button

class Map:
    def __init__(self, window, blockSize, res_w, res_h):
        self.blockSize = blockSize
        self.window = window
        self.res_w = res_w
        self.res_h = res_h
        self.new_build_pos_x = None
        self.new_build_pos_y = None
        self.object_selected = 0
        self.active_troop_button = None
        self.gridmap = self.grid()

    'Create grid from blocks'
    def grid(self):
        gridmap = []
        for x in range(0, self.res_w, self.blockSize):
            grid_map_line = []
            for y in range(0, self.res_h, self.blockSize):
                if ((self.res_w - x) <= (3 * self.blockSize)) or ((self.res_h - y) <= (3 * self.blockSize)):
                    rect = Rect(x, y, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, (110, 110, 110), rect)
                    grid_map_line.append('p')
                else:
                    rect = Rect(x, y, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, (110, 110, 110), rect, 1)
                    grid_map_line.append(0)
            gridmap.append(grid_map_line)
        print(gridmap)
        return gridmap

    'Returns object that is located in gridmap position.'
    def get_grid_object(self, x, y):
        return self.gridmap[x][y]

    'Changes object in gridmap.'
    def change_grid_object(self, x, y, obj):
        self.gridmap[x][y] = obj

    'Converts pixels coordinates to grid coordinates.'
    def get_pos_in_grid(self, pos):
        x = math.floor(pos[0] / self.blockSize)
        y = math.floor(pos[1] / self.blockSize)
        return x,y

    'Checks if clicked grid is empty.'
    def position_empty(self, pos):
        x_pos_block, y_pos_block = self.get_pos_in_grid(pos)
        try:
            if self.gridmap[x_pos_block][y_pos_block] == 0:
                self.new_build_pos_x = x_pos_block
                self.new_build_pos_y = y_pos_block
                return 1
            return 0
        except IndexError:
            print("Outside of grid.")

    'Creates new building object and sets it to map.'
    def create_building(self):
        new_building = Building((self.new_build_pos_x, self.new_build_pos_y),
                                self.window,
                                self.blockSize,
                                self.res_w,
                                self.res_h
                                )
        self.change_grid_object(self.new_build_pos_x, self.new_build_pos_y, new_building)


    'Sets building to select-position.'
    def select_building(self, pos):
        x, y = self.get_pos_in_grid(pos)

        # If IndexError occurs, it means that player clicked outside gridmap.
        try:
            grid_object = self.get_grid_object(x, y)
            if str(type(grid_object)) == "<class 'building.Building'>" and (self.object_selected == 0):
                self.object_selected = 1
                grid_object.select(1)
                self.active_troop_button = Button(4, 14, 30, 2, "Troop", self.window)

                # Show button for user
                self.change_grid_object(4, 14, 'b')
                self.change_grid_object(5, 14, 'b')
                return

            if str(type(grid_object)) == "<class 'building.Building'>" and self.object_selected and grid_object.selected:
                self.object_selected = 0
                grid_object.select(0)

                # Remove button
                self.active_troop_button.remove_button()
                self.active_troop_button = None
                self.change_grid_object(4, 14, 'p')
                self.change_grid_object(5, 14, 'p')

        except IndexError:
            print("Not active block at the moment.")
            return


