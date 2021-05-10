import pygame
from random import choice

pygame.init()


def oposite_direction(direction):
        if direction == 'top':
            return 'bottom'
        if direction == 'bottom':
            return 'top'
        if direction == 'left':
            return 'right'
        if direction == 'right':
            return 'left'

class Binary:
    def __init__(self, grid_list):
        self.grid_list = grid_list
        
        self.directions = ['top', 'left']

        self.index_i = 0
        self.index_j = 0
        self.actual = grid_list[self.index_i][self.index_j]

        self.end = False
    def generate(self):
        if not self.end:
            self.actual.visited = True
            print(self.index_i, self.index_j)
            if self.index_i > 0 and self.index_j > 0:
                direction = choice(self.directions)
                o_direction = oposite_direction(direction)
                self.actual.walls[direction] = False
                self.actual.edges[direction].node.walls[o_direction] = False
            else:        
                for wall in self.actual.walls:
                    if self.index_j == 0:
                        if wall == 'right' and  self.index_i < len(self.grid_list) - 1:
                            op_wall = oposite_direction(wall)
                            self.actual.walls[wall] = False
                            self.actual.edges[wall].node.walls[op_wall] = False
                    if self.index_i == 0:
                        if wall == 'bottom' and self.index_j < len(self.grid_list[self.index_i]) - 1: 
                            op_wall = oposite_direction(wall)
                            self.actual.walls[wall] = False
                            self.actual.edges[wall].node.walls[op_wall] = False

            self.index_i += 1
            if self.index_i > len(self.grid_list) - 1:
                self.index_i = 0           
                self.index_j += 1
            
            if self.index_j > len(self.grid_list[self.index_i]) - 1:
                self.end = True
                return

            self.actual = self.grid_list[self.index_i][self.index_j] 

    def draw_grid(self, window, grid_list):
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):

                if grid_list[i][j].visited == True:
                    pygame.draw.rect(window, (50, 50, 200), grid_list[i][j].rect)

                    if grid_list[i][j].walls['top']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.topright, width=2)
                    if grid_list[i][j].walls['bottom']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.bottomleft, grid_list[i][j].rect.bottomright, width=2)
                    if grid_list[i][j].walls['left']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.bottomleft, width=2)
                    if grid_list[i][j].walls['right']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topright, grid_list[i][j].rect.bottomright, width=2)

                if not self.end:
                    pygame.draw.rect(window, (200, 0, 0), self.actual.rect)

