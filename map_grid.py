from pygame import Rect
import pygame
import math
from building import Building
from button import Button
from unit import Unit

class Map:
    def __init__(self, window, blockSize, res_w, res_h, sprite_list):
        self.blockSize = blockSize
        self.window = window
        self.res_w = res_w
        self.res_h = res_h
        self.sprite_list = sprite_list
        self.new_build_pos_x = None
        self.new_build_pos_y = None
        self.object_selected = 0
        self.active_troop_button = None
        self.troops = []
        self.gridmap = self.grid()
        self.active_building = None

    'Read map from a file'
    def grid(self):
        gridmap = []
        with open("map.txt", "r") as map:
            for line in map:
                line = line[:-1]
                map_line = []
                for i in line.split(" "):
                    if i == '0':
                        map_line.append(int(i))
                    else:
                        map_line.append(i)
                gridmap.append(map_line)
        return gridmap

    'Returns object that is located in gridmap position.'
    def get_grid_object(self, x, y):
        return self.gridmap[x][y]

    'Changes object in gridmap.'
    def change_grid_object(self, x, y, obj):
        self.gridmap[x][y] = obj

    def get_grid_dimensions(self):
        w = self.res_w / self.blockSize
        h = self.res_h / self.blockSize
        return [int(w), int(h)]


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


    def troop_list_update(self, troop):
        lista = self.troops
        lista.append(troop)
        self.troops = lista


    'Sets building to select-position.'
    def select_building(self, pos):
        x, y = self.get_pos_in_grid(pos)
        # If IndexError occurs, it means that player clicked outside gridmap.
        try:
            grid_object = self.get_grid_object(x, y)
            if str(type(grid_object)) == "<class 'building.Building'>" and (self.object_selected == 0):
                self.object_selected = 1
                grid_object.select(1)
                dim = self.get_grid_dimensions()
                self.active_troop_button = Button(3, dim[1] - 2, 30, 2, "Troop", self.window)

                # Show button for user

                self.change_grid_object(5, dim[1] - 3, 'b')
                self.change_grid_object(6, dim[1] - 3, 'b')
                self.change_grid_object(5, dim[1] - 2, 'b')
                self.change_grid_object(6, dim[1] - 2, 'b')

                self.active_building = grid_object
                return

            if str(type(grid_object)) == "<class 'building.Building'>" and self.object_selected and grid_object.selected:
                self.object_selected = 0
                grid_object.select(0)

                # Remove button
                self.active_troop_button.remove_button()
                self.active_troop_button = None

                dim = self.get_grid_dimensions()
                self.change_grid_object(5, dim[1] - 3, 'p')
                self.change_grid_object(6, dim[1] - 3, 'p')
                self.change_grid_object(5, dim[1] - 2, 'p')
                self.change_grid_object(6, dim[1] - 2, 'p')
                self.active_building = None

            # Create troop
            if str(type(self.active_troop_button)) == "<class 'button.Button'>" and grid_object == 'b':
                troop = Unit(self.active_building.get_position(), self.window, self.blockSize, self.gridmap)
                self.troop_list_update(troop)

        except IndexError:
            print("Not active block at the moment.")
            return

    def update_troops(self):
        if self.troops != 0:
            for i in self.troops:
                i.move()

    'Draws lines to GUI.'
    def draw_line(self, x1, y1, x2, y2, col):
        pygame.draw.lines(self.window, col, True,
                          [(x1, y1), (x2, y2)], 1)


    'Update map in every iteration'
    def update(self):
        self.window.fill((255, 255, 204))
        for index_i, i in enumerate(self.gridmap):
            for index_j, j in enumerate(i):

                # Grid object empty.
                if j == 0:
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((255, 255, 204)), rect, 1)

                # Grid object building and not active.
                if str(type(j)) == "<class 'building.Building'>":

                    myimage = self.sprite_list["tent"]
                    imagerect = Rect(index_i * self.blockSize,
                                               index_j * self.blockSize,
                                               self.blockSize,
                                               self.blockSize
                                               )

                    self.window.blit(myimage, imagerect)

                # Grid object button.
                if j == 'b':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)
                    dim = self.get_grid_dimensions()
                    myimage = self.sprite_list["miner_face"]
                    imagerect = Rect(5 * self.blockSize,
                                     (dim[1] - 3) * self.blockSize,
                                     self.blockSize,
                                     self.blockSize
                                     )

                    self.window.blit(myimage, imagerect)

                # Resource wood
                if j == 'r':
                    myimage = self.sprite_list["resource_1"]
                    imagerect = Rect(index_i * self.blockSize,
                                            index_j * self.blockSize,
                                            self.blockSize,
                                            self.blockSize
                                            )

                    self.window.blit(myimage, imagerect)

                # Resource gold
                if j == 'g':
                    myimage = self.sprite_list["gold"]
                    imagerect = Rect(index_i * self.blockSize,
                                    index_j * self.blockSize,
                                    self.blockSize,
                                    self.blockSize
                                    )

                    self.window.blit(myimage, imagerect)

                # Resource gold
                if j == 'cr':
                    myimage = self.sprite_list["crystal"]
                    imagerect = Rect(index_i * self.blockSize,
                                    index_j * self.blockSize,
                                    self.blockSize,
                                    self.blockSize
                                    )

                    self.window.blit(myimage, imagerect)


                # Grid object active building
                if str(type(j)) == "<class 'building.Building'>" and self.active_building == j:
                    myimage = self.sprite_list["tent_selected"]
                    imagerect = Rect(index_i * self.blockSize,
                                            index_j * self.blockSize,
                                            self.blockSize,
                                            self.blockSize
                                            )
                    self.window.blit(myimage, imagerect)

                # Draw panel
                if j == 'p':
                    myimage = self.sprite_list["panel_3"]
                    imagerect = Rect(index_i * self.blockSize,
                                     index_j * self.blockSize,
                                     self.blockSize,
                                     self.blockSize
                                     )
                    self.window.blit(myimage, imagerect)

                if j == 'pe':
                    myimage = self.sprite_list["panel_edge"]
                    imagerect = Rect(index_i * self.blockSize,
                                     index_j * self.blockSize,
                                     self.blockSize,
                                     self.blockSize
                                     )
                    self.window.blit(myimage, imagerect)

                # Log
                if j == 'l':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)
                    myimage = self.sprite_list["log"]
                    imagerect = Rect(index_i * self.blockSize,
                                     index_j * self.blockSize,
                                     self.blockSize,
                                     self.blockSize
                                     )
                    self.window.blit(myimage, imagerect)

                # Gold panel
                if j == 'gp':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)
                    myimage = self.sprite_list["gold_panel"]
                    imagerect = Rect(index_i * self.blockSize,
                                    index_j * self.blockSize,
                                    self.blockSize,
                                    self.blockSize
                                    )
                    self.window.blit(myimage, imagerect)

                # Gold panel
                if j == 'cp':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)
                    myimage = self.sprite_list["crystal_panel"]
                    imagerect = Rect(index_i * self.blockSize,
                                    index_j * self.blockSize,
                                    self.blockSize,
                                    self.blockSize
                                    )
                    self.window.blit(myimage, imagerect)


                # Corner sprite.
                if j == 'c':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)
                    myimage = self.sprite_list["corner_1"]
                    imagerect = Rect(index_i * self.blockSize,
                                     index_j * self.blockSize,
                                     self.blockSize,
                                     self.blockSize
                                     )
                    self.window.blit(myimage, imagerect)

                # Different panel block.
                if j == 'c1':
                    rect = Rect(index_i * self.blockSize, index_j * self.blockSize, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.window, ((100, 100, 100)), rect)
                    pygame.draw.rect(self.window, ((0, 0, 0)), rect, 1)