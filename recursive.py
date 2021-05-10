import pygame
from random import choice

pygame.init()

class Recursive:
    def __init__(self, actual):
        self.count_index = -1
        self.visited_nodes = []
        self.actual = actual
        self.end = False

    def generate(self):
        if not self.actual in self.visited_nodes: 
            self.visited_nodes.append(self.actual)
            self.actual.visited = True
            self.count_index += 1

        not_visited_edges = []
        for edge in self.actual.edges:
            if not self.actual.edges[edge].node.visited:
                not_visited_edges.append(edge)
        
        if len(not_visited_edges) > 0:
            direction = choice(not_visited_edges)
            self.actual.walls[direction] = False
            self.actual = self.actual.edges[direction].node
            self.actual.walls[self.actual.oposite_direction(direction)] = False

        else:
            self.count_index -= 1
            self.visited_nodes.remove(self.actual)
            try:
                self.actual = self.visited_nodes[self.count_index]
            except:
                self.end = True
                return

    def draw_grid(self, window, grid_list):
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):

                if grid_list[i][j].visited == True:
                    pygame.draw.rect(window, (50, 50, 200), grid_list[i][j].rect)

                    if grid_list[i][j] in self.visited_nodes:
                        pygame.draw.rect(window, (100, 100, 200), grid_list[i][j].rect)

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

                
            
        

