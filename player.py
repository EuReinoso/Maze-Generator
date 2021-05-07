import pygame

pygame.init()

class Player:
    def __init__(self, start_node, color):
        self.rect = start_node.rect
        self.color = color

        self.actual = start_node

        self.right = False
        self.left = False
        self.down = False
        self.up = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect, border_radius= 20)

    def set_dir(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_DOWN:
                self.down = True
            if event.key == pygame.K_UP:
                self.up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_DOWN:
                self.down = False
            if event.key == pygame.K_UP:
                self.up = False
        
    def move(self, grid_list):
        for i in range(len(grid_list)):
            for j in range(len(grid_list[i])):
                if self.rect == grid_list[i][j].rect:
                    self.actual = grid_list[i][j]
        
        if self.right and not self.actual.walls['right']:
            self.rect = self.actual.edges['right'].node.rect

        if self.left and not self.actual.walls['left'] :
            self.rect = self.actual.edges['left'].node.rect

        if self.down and not self.actual.walls['down']:
            self.rect = self.actual.edges['down'].node.rect

        if self.up and not self.actual.walls['top']:
            self.rect = self.actual.edges['top'].node.rect


