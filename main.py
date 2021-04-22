import pygame, sys
import numpy as np
from recursive import Recursive

pygame.init()

class Node:
    def __init__(self, rect):
        self.rect = rect
        self.edges = []
        self.visited = False

    

class Edge:
    def __init__(self, node):
        self.node = node
        

WINDOW_SIZE = (640, 480)

tile_size = 20
grid_list = np.empty((WINDOW_SIZE[0]//tile_size, WINDOW_SIZE[1]//tile_size), dtype= object)

def init_nodes():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            rect = pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size)
            grid_list[i][j] = Node(rect)

def init_edges():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            if i > 0:
                grid_list[i][j].edges.append(Edge(grid_list[i - 1][j]))
            if i < len(grid_list) - 1:
                grid_list[i][j].edges.append(Edge(grid_list[i + 1][j]))
            if j > 0:
                grid_list[i][j].edges.append(Edge(grid_list[i][j - 1]))
            if j < len(grid_list[0]) - 1:
                grid_list[i][j].edges.append(Edge(grid_list[i][j + 1]))

def draw():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            if grid_list[i][j].visited == True:
                pygame.draw.rect(window, (200, 200, 200), grid_list[i][j].rect)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Maze')



init_nodes()
init_edges()

re = Recursive(grid_list[0][0])

fps= 30
time = pygame.time.Clock()
while True:
    
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    re.generate(window)
    pygame.display.update()
    time.tick(fps)