import pygame
from random import choice

pygame.init()

class Recursive:
    def __init__(self, actual):
        self.count_index = -1
        self.visited_nodes = []
        self.actual = actual

    def generate(self, window):
        if not self.actual in self.visited_nodes: 
            self.visited_nodes.append(self.actual)
            self.actual.visited = True
            self.count_index += 1

        pygame.draw.rect(window, (200,0,0), self.actual.rect)

        not_visited_edges = []

        for edge in self.actual.edges:
            if not edge.node.visited:
                not_visited_edges.append(edge)
        
        if len(not_visited_edges) > 0:
            self.actual = choice(not_visited_edges).node
            
        else:
            self.count_index -= 1
            self.visited_nodes.remove(self.actual)
            self.actual = self.visited_nodes[self.count_index]
        

