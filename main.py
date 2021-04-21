import pygame, sys
import numpy as np

pygame.init()

class Node:
    def __init__(self, rect):
        self.rect = rect
        self.adjacents = []

WINDOW_SIZE = (640, 480)


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