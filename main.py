import pygame, sys
import numpy as np
from recursive import Recursive
from kruskal import Kruskal
from player import Player
from button import Button

pygame.init()
pygame.font.init()

WINDOW_SIZE = (642, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Maze')

tile_size = 40
grid_i = WINDOW_SIZE[0]//tile_size
grid_j = (WINDOW_SIZE[1] - 48)//tile_size
grid_list = np.empty((grid_i , grid_j), dtype= object)

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

def tile_size_select(buttons, tiles, event, mx, my):
    global tile_size
    for i in range(len(buttons)):
        if buttons[i].click(event, mx, my):
            tile_size = tiles[i]
            buttons[i].selected = True
            for b  in range(len(buttons)):
                if buttons[b] !=  buttons[i]:
                    buttons[b].selected = False
            
def maze_init():

    fps= 60
    time = pygame.time.Clock()
    loop = True

    init_nodes()
    init_edges()

    re = Recursive(grid_list[0][0])
    kr = Kruskal(grid_list)
    algorithm = kr

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

        algorithm.generate()
        
        if not algorithm.end:
            draw_text('Generating...', window, 30, (200, 200, 200), (window.get_rect().center[0], 448))
        
        else:
            play_button.draw(window)
            if play_button.on_up:
                loop = False
                play(algorithm)

        algorithm.draw_grid(window, grid_list)
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
        else:
            game_time += time_count

        algorithm.draw_grid(window, grid_list)
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

    tile_select_buttons_rect = []
    tile_select_buttons_count = 3
    tile_select_buttons_pos = [110, 200]

    for i in range(tile_select_buttons_count):
        tile_select_buttons_rect.append(pygame.Rect(tile_select_buttons_pos[0], tile_select_buttons_pos[1], 120, 30))
        tile_select_buttons_pos[0] += 150
    
    tile_select_buttons = [
            Button(tile_select_buttons_rect[0], text= 'Small'),
            Button(tile_select_buttons_rect[1], text= 'Medium'),
            Button(tile_select_buttons_rect[2], text= 'Large')
        ]
    
    tile_select_buttons[1].selected = True

    while loop:
        window.fill((0, 0, 50))

        mx, my =pygame.mouse.get_pos()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button1.click(event, mx, my):
                maze_init()
            tile_size_select(tile_select_buttons, [80, 40, 20], event, mx, my)
                

        draw_text('MENU', window, 100, (200, 200, 200), (window.get_rect().center[0], 100))
        draw_text('Select maze size', window, 30, (200, 200, 200), (window.get_rect().center[0], 170))

        button1.draw(window)         
        
        for button in tile_select_buttons:
            if button.selected:
                button.color = (50, 150, 50)
            else:
                button.color = (100, 100, 100)

            button.draw(window)

        pygame.display.update()
        time.tick(fps)


menu()