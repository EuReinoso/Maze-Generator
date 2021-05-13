from numpy.core.numeric import True_
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

class Prim:
    def __init__(self, actual):
        self.actual = actual
        self.walls_list = []
        self.end = False
        
        self.add_walls_list(self.actual)

    def add_walls_list(self, actual):
        for wall in actual.walls_obj:
            wall_obj = actual.walls_obj[wall]
            if wall in actual.edges:
                edge = wall_obj.node.edges[wall].node
                if not edge.visited:
                    self.walls_list.append(wall_obj)

    def generate(self):
        if len(self.walls_list) > 0:
            wall = choice(self.walls_list)
            direction = wall.direction
            op_direction = oposite_direction(direction)
            node = wall.node
            edge = node.edges[direction].node

            if not edge.visited:
                node.walls[direction] = False
                edge.walls[op_direction] = False

                edge.visited = True

                self.add_walls_list(edge)
            
            self.walls_list.remove(wall)
        else:
            self.end = True


    def draw_grid(self, window, grid_list):
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):

                if grid_list[i][j].visited == True:
                    pygame.draw.rect(window, (50, 50, 200), grid_list[i][j].rect)

                    for wall in self.walls_list:
                        if wall.node == grid_list[i][j]:
                            pygame.draw.rect(window, (200, 0, 0), grid_list[i][j].rect)

                    if grid_list[i][j].walls['top']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.topright, width=2)
                    if grid_list[i][j].walls['bottom']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.bottomleft, grid_list[i][j].rect.bottomright, width=2)
                    if grid_list[i][j].walls['left']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.bottomleft, width=2)
                    if grid_list[i][j].walls['right']:
                        pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topright, grid_list[i][j].rect.bottomright, width=2)

        

