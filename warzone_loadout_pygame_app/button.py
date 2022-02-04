import pygame

pygame.font.init()
BUTTON_FONT = pygame.font.Font(None, 50)

BLACK, WHITE = (0,0,0), (255,255,255)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image.set_alpha(float(255 * 0.9))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.clicked = False

    def draw_image(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
                # print('clicked')

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action