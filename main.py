import pygame, sys
import numpy as np
from recursive import Recursive
from player import Player

pygame.init()
pygame.font.init()

class Node:
    def __init__(self, rect):
        self.rect = rect
        self.edges = {}
        self.visited = False

        self.walls = {'top' : True, 'down' : True, 'left': True, 'right' : True}
        
    
    def oposite_direction(self, direction):
        if direction == 'top':
            return 'down'
        if direction == 'down':
            return 'top'
        if direction == 'left':
            return 'right'
        if direction == 'right':
            return 'left'
class Edge:
    def __init__(self, node):
        self.node = node

WINDOW_SIZE = (640, 480)

tile_size = 40
grid_list = np.empty((WINDOW_SIZE[0]//tile_size, WINDOW_SIZE[1]//tile_size), dtype= object)

player_rect = pygame.Rect(0, 0, tile_size, tile_size)
player = Player(player_rect, (200, 0, 0))

def init_nodes():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[i])):
            rect = pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size)
            grid_list[i][j] = Node(rect)

def init_edges():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[i])):
            if i > 0:
                grid_list[i][j].edges['left'] = Edge(grid_list[i - 1][j])
            if i < len(grid_list) - 1:
                grid_list[i][j].edges['right'] = Edge(grid_list[i + 1][j])
            if j > 0:
                grid_list[i][j].edges['top'] = Edge(grid_list[i][j - 1])
            if j < len(grid_list[0]) - 1:
                grid_list[i][j].edges['down'] = Edge(grid_list[i][j + 1])

def draw_grid():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            if grid_list[i][j].visited == True:
                pygame.draw.rect(window, (50, 50, 200), grid_list[i][j].rect)

                if grid_list[i][j].walls['top']:
                    pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.topright, width=2)
                if grid_list[i][j].walls['down']:
                    pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.bottomleft, grid_list[i][j].rect.bottomright, width=2)
                if grid_list[i][j].walls['left']:
                    pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topleft, grid_list[i][j].rect.bottomleft, width=2)
                if grid_list[i][j].walls['right']:
                    pygame.draw.line(window, (200,200,200), grid_list[i][j].rect.topright, grid_list[i][j].rect.bottomright, width=2)

                if not re.end:
                    pygame.draw.rect(window, (200,0,0), re.actual.rect)

def draw_text(text, surface, size, color, pos):
    font = pygame.font.SysFont(None, size)
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.topleft = pos
    surface.blit(text_render, text_rect)

                
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Maze')

init_nodes()
init_edges()

re = Recursive(grid_list[0][0])


def maze_init():

    fps= 60
    time = pygame.time.Clock()
    loop = True

    while loop:
        
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        re.generate(window)
        
        if re.end:
            loop = False
            play()

        draw_grid()
        pygame.display.update()
        time.tick(fps)

def play():
    fps= 7
    time = pygame.time.Clock()
    loop = True

    
    while loop:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.set_dir(event)
        
        draw_grid()

        player.move(grid_list)
        player.draw(window)

        pygame.display.update()
        time.tick(fps)



maze_init()