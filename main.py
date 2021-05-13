"""
add algorithm on 'algorithm_names', algorithms_init, menu/algorithm_select_buttons,  
"""

import pygame, sys
import numpy as np
from algorithms.recursive import Recursive
from algorithms.kruskal import Kruskal
from algorithms.binary import Binary
from algorithms.prim import Prim
from player import Player
from button import Button

pygame.init()
pygame.font.init()

WINDOW_SIZE = (642, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Maze Generator')

tile_size = 40
grid_i = WINDOW_SIZE[0]//tile_size
grid_j = (WINDOW_SIZE[1] - 48)//tile_size
grid_list = np.empty((grid_i , grid_j), dtype= object)

algorithms = {}
algorithm_names = ['Recursive', 'Kruskal', 'Binary', 'Prim']

class Node:
    def __init__(self, rect):
        self.rect = rect
        self.edges = {}
        self.visited = False

        self.walls = {'top' : True, 'bottom' : True, 'left': True, 'right' : True}
        self.walls_rect, self.walls_obj = self.walls_rect_init()

    def walls_rect_init(self):
        walls_rect = {}
        walls_obj = {}

        walls_rect['top']       = pygame.Rect(self.rect.topleft[0],self.rect.topleft[1],
                    self.rect.width, 2)
        walls_rect['left']      = pygame.Rect(self.rect.topleft[0],self.rect.topleft[1],
                    2, self.rect.height)
        walls_rect['bottom']    = pygame.Rect(self.rect.bottomleft[0],self.rect.bottomleft[1],
                    self.rect.width, 2)   
        walls_rect['right']     = pygame.Rect(self.rect.topright[0],self.rect.topright[1],
                    2, self.rect.height)

        walls_obj['top']    = Wall(walls_rect['top'], 'top', self)
        walls_obj['left']   = Wall(walls_rect['left'], 'left', self)
        walls_obj['bottom'] = Wall(walls_rect['bottom'], 'bottom', self)
        walls_obj['right']  = Wall(walls_rect['right'], 'right', self)

        return walls_rect, walls_obj

    def oposite_direction(self, direction):
        if direction == 'top':
            return 'bottom'
        if direction == 'bottom':
            return 'top'
        if direction == 'left':
            return 'right'
        if direction == 'right':
            return 'left'
class Edge:
    def __init__(self, node):
        self.node = node

class Wall:
    def __init__(self, rect, direction, node):
        self.rect = rect
        self.direction = direction
        self.node = node

def init_nodes():
    global tile_size, grid_i, grid_j, grid_list
    grid_i = WINDOW_SIZE[0]//tile_size
    grid_j = (WINDOW_SIZE[1] - 48)//tile_size
    grid_list = np.empty((grid_i , grid_j), dtype= object)
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
            if j < len(grid_list[i]) - 1:
                grid_list[i][j].edges['bottom'] = Edge(grid_list[i][j + 1])

def draw_text(text, surface, size, color, pos):
    font = pygame.font.SysFont(None, size)
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    surface.blit(text_render, text_rect)

def tile_size_select(buttons, event, mx, my, tiles,):
    global tile_size
    for i in range(len(buttons)):
        if buttons[i].click(event, mx, my):
            tile_size = tiles[i]
            buttons[i].selected = True
            for b  in range(len(buttons)):
                if buttons[b] !=  buttons[i]:
                    buttons[b].selected = False

def algorithm_select(buttons,  event, mx, my, name):
    for i in range(len(buttons)):
        if buttons[i].click(event, mx, my):
            name = algorithm_names[i]
            buttons[i].selected = True
            for b in range(len(buttons)):
                if buttons[b] != buttons[i]:
                    buttons[b].selected = False
    return name

def create_select_buttons(quant, pos, size, space= 30, texts= []):
    select_buttons = []

    for i in range(quant):
        rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        button = Button(rect, text= texts[i])
        select_buttons.append(button)
        pos[0] += size[0] + space
    
    return select_buttons

def algorithms_init():
    algorithms_list = [
        Recursive(grid_list[0][0]), 
        Kruskal(grid_list),
        Binary(grid_list),
        Prim(grid_list[0][0])]
    
    algorithms = {}
    for i in range(len(algorithms_list)):
        algorithms[algorithm_names[i]] = algorithms_list[i]
    
    return algorithms

def maze_init(name):

    fps= 60
    time = pygame.time.Clock()
    loop = True

    init_nodes()
    init_edges()

    algorithms = algorithms_init()
    algorithm = None

    for alg_name in algorithms:
        if alg_name == name:
            algorithm = algorithms[alg_name]

    play_button_rect = pygame.Rect(window.get_rect().center[0] - (200/ 2), 430, 200, 40)
    play_button = Button(play_button_rect, text= 'PLAY')

    menu_button_rect = pygame.Rect(10, 440, 100, 30)
    menu_button = Button(menu_button_rect, text= '< MENU')
    while loop:
        
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            play_button.click(event, mx, my)
            if menu_button.click(event, mx, my):
                loop = False

        algorithm.generate()
        
        if not algorithm.end:
            draw_text('Generating...', window, 30, (200, 200, 200), (window.get_rect().center[0], 448))
        
        else:
            play_button.draw(window)
            if play_button.on_up:
                loop = False
                play(algorithm)

        algorithm.draw_grid(window, grid_list)

        menu_button.draw(window)
        pygame.display.update()
        time.tick(fps)

def play(algorithm):
    fps= 7
    time = pygame.time.Clock()
    loop = True

    game_time = 0
    time_count = 1/ fps

    begin_node = grid_list[0][0]
    player = Player(begin_node, (200, 0, 0))

    objective = grid_list[-1][-1]

    menu_button_rect = pygame.Rect(10, 440, 100, 30)
    menu_button = Button(menu_button_rect, text= '< MENU')
    while loop:
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.set_dir(event)
            if menu_button.click(event, mx, my):
                loop = False

        if player.actual == objective:
            draw_text('YOU WIN!', window, 40, (200, 200, 200), (window.get_rect().center[0], 440) )
        else:
            game_time += time_count

        algorithm.draw_grid(window, grid_list)
        menu_button.draw(window)
        draw_text('Time: ' + str(round(game_time, 2)), window, 30, (200, 200, 200), (580, 440))

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

    tile_select_buttons = create_select_buttons(3, [110, 200], [120, 30], texts= ['Small', 'Medium', 'Large'])
    tile_select_buttons[1].selected = True

    algorithm_select_buttons = create_select_buttons(4, [90, 300], [100, 30], texts= algorithm_names )
    algorithm_select_buttons[0].selected = True
    name = algorithm_names[0]
    while loop:
        window.fill((0, 0, 50))

        mx, my =pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button1.click(event, mx, my):
                maze_init(name)
            tile_size_select(tile_select_buttons, event, mx, my, [80, 40, 20])
            name = algorithm_select(algorithm_select_buttons, event, mx, my, name)
                

        draw_text('MAZE GENERATOR', window, 70, (200, 200, 200), (window.get_rect().center[0], 100))
        draw_text('Select maze size', window, 30, (200, 200, 200), (window.get_rect().center[0], 170))
        draw_text('Select algorithm', window, 30, (200, 200, 200), (window.get_rect().center[0], 270))

        button1.draw(window)         
        
        for button in tile_select_buttons:
            if button.selected:
                button.color = (50, 150, 50)
            else:
                button.color = (100, 100, 100)

            button.draw(window)
        
        for button in algorithm_select_buttons:
            if button.selected:
                button.color = (50, 150, 50)
            else:
                button.color = (100, 100, 100)

            button.draw(window)

        pygame.display.update()
        time.tick(fps)

menu()