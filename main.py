import pygame, sys
import numpy as np

pygame.init()

class Node:
    def __init__(self, rect):
        self.rect = rect
        self.adjacents = []

WINDOW_SIZE = (640, 480)

tile_size = 20
grid_list = np.empty((WINDOW_SIZE[0]//tile_size, WINDOW_SIZE[1]//tile_size), dtype= object)

def init_nodes():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            rect = pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size)
            grid_list[i][j] = Node(rect)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Maze')

init_nodes()
while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()