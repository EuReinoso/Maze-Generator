import pygame

pygame.init()

class Button:
    def __init__(self, rect, color= (128, 128, 128), text= '', text_color= (200, 200, 200)):
        self.rect = rect
        self.color = color
        self.text = text
        self.text_size = rect.height
        self.text_color = text_color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        if self.text != '':
            self.draw_text(window)

    def draw_text(self, surface):
        font = pygame.font.SysFont(None, self.text_size)
        text_render = font.render(self.text, 1, self.text_color)
        text_rect = text_render.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text_render, text_rect)

    def click(self, event, mx, my, color_change = False, color_down = (100, 100, 200), color_up= (128, 128, 128)):
        if self.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if color_change:
                        self.color = color_down

                    return True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if color_change:
                        self.color = color_up

                    return True
                