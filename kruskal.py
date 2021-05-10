import pygame
from random import choice

pygame.init()

class Kruskal:
    def __init__(self, grid_list):
        self.sets = self.sets_init(grid_list)
        self.size = len(self.sets)
        self.count_visiteds = 0
        self.walls = self.walls_list_init(grid_list)
        self.end = False

    def sets_init(self, grid_list):
        sets = []
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):
                sets.append({grid_list[i][j]})
        return sets

    def walls_list_init(self, grid_list):
        walls = []
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):
                for k in grid_list[i][j].walls_obj:
                    wall = grid_list[i][j].walls_obj[k]
                    direction = wall.direction
                    if direction == 'left' and i > 0:
                        walls.append(wall)
                    if direction == 'right' and i < len(grid_list) - 1:
                        walls.append(wall)
                    if direction == 'top' and j > 0:
                        walls.append(wall)
                    if direction == 'bottom' and j < len(grid_list[i]) - 1:
                        walls.append(wall)
                    
        return walls
                

    def generate(self):
        if not len(self.walls) > 0 or not self.count_visiteds < self.size:
            self.end = True
            return

        wall = choice(self.walls)    
        node = wall.node
        direction = wall.direction
        oposite_direction = node.oposite_direction(direction)

        if direction == 'top':
            edge = node.edges['top'].node
        if direction == 'left':
            edge = node.edges['left'].node
        if direction == 'bottom':
            edge = node.edges['bottom'].node
        if direction == 'right':
            edge = node.edges['right'].node
        
        index1 = 0
        for i in range(len(self.sets)):
            if node in self.sets[i]:
                index1 = i

        index2 = 0
        for i in range(len(self.sets)):
            if edge in self.sets[i]:
                index2 = i

        if not index1 == index2:
            self.sets.append(self.sets[index1] | self.sets[index2])

            node.walls[direction] = False
            edge.walls[oposite_direction] = False

            if not node.visited:
                node.visited = True
                self.count_visiteds += 1
            if not edge.visited:
                edge.visited = True
                self.count_visiteds += 1
        
        self.walls.remove(wall)

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


    





