import pygame, sys
import numpy as np
from recursive import Recursive
from player import Player
from button import Button

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

WINDOW_SIZE = (642, 480)

tile_size = 80
grid_i = WINDOW_SIZE[0]//tile_size
grid_j = (WINDOW_SIZE[1] - 48)//tile_size
grid_list = np.empty((grid_i , grid_j), dtype= object)

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
    text_rect.center = pos
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

    play_button_rect = pygame.Rect(window.get_rect().center[0] - (200/ 2), 430, 200, 40)
    play_button = Button(play_button_rect, text= 'PLAY')
    while loop:
        
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            play_button.click(event, mx, my)

        re.generate(window)
        
        if not re.end:
            draw_text('Generating...', window, 30, (200, 200, 200), (window.get_rect().center[0], 448))
        
        else:
            play_button.draw(window)
            if play_button.on_up:
                loop = False
                play()

        draw_grid()
        pygame.display.update()
        time.tick(fps)

def play():
    fps= 7
    time = pygame.time.Clock()
    loop = True

    begin_node = grid_list[0][0]
    player = Player(begin_node, (200, 0, 0))

    objective = grid_list[-1][-1]

    menu_button_rect = pygame.Rect(10, 430, 150, 40)
    menu_button = Button(menu_button_rect, text= '< MENU')
    while loop:
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.set_dir(event)
            menu_button.click(event, mx, my)

        if player.actual == objective:
            draw_text('YOU WIN!', window, 40, (200, 200, 200), (window.get_rect().center[0], 440) )
            menu_button.draw(window)

            if menu_button.on_up:
                loop= False

        draw_grid()

        player.move(grid_list)
        player.draw(window)

        pygame.draw.rect(window, (0, 0, 0), objective.rect, border_radius= 20)
        pygame.display.update()
        time.tick(fps)

def menu():
    fps= 60
    time = pygame.time.Clock()
    loop = True

    button1_rect = pygame.Rect(220, 400, 200, 40)
    button1 = Button(button1_rect, text= 'Generate!')

    while loop:
        window.fill((0, 0, 50))

        mx, my =pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button1.click(event, mx, my):
                maze_init()
                

        draw_text('MENU', window, 100, (200, 200, 200), (window.get_rect().center[0], 100))    
        button1.draw(window)         
        
        pygame.display.update()
        time.tick(fps)


menu()