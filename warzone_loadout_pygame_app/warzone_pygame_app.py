from turtle import width
import pygame
import os
import button
import sys
import weapon_classes

pygame.init()

class Game_State:
    def __init__(self):
        self.state = "main_menu"

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MW_BUTTON.draw_image(WIN) == True:
                self.state = "mw_screen"
            if CW_BUTTON.draw_image(WIN) == True:
                self.state = "cw_screen"
            if VG_BUTTON.draw_image(WIN) == True:
                self.state = "vg_screen"
            if CREATE_LOADOUT_BUTTON.draw_image(WIN) == True:
                self.state = "create_loadout_screen"

        draw_home_window()

    def mw_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if HOME_BUTTON.draw_image(WIN) == True:
                self.state = "main_menu"

        draw_mw_window()

    def cw_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if HOME_BUTTON.draw_image(WIN) == True:
                self.state = "main_menu"

        draw_cw_window()

    def vg_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if HOME_BUTTON.draw_image(WIN) == True:
                self.state = "main_menu"

        draw_vg_window()
    
    def create_loadout(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if HOME_BUTTON.draw_image(WIN) == True:
                self.state = "main_menu"

        draw_create_loadout_window()

    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        if self.state == "mw_screen":
            self.mw_screen()
        if self.state == "cw_screen":
            self.cw_screen()
        if self.state == "vg_screen":
            self.vg_screen()
        if self.state == "create_loadout_screen":
            self.create_loadout()


            
game_state = Game_State()

WIDTH, HEIGHT = 1280, 721
BLACK, WHITE = (0, 0, 0), (255, 255, 255)

TITLE_FONT = pygame.font.Font(None, 50)
LABEL_FONT = pygame.font.Font(None, 30)

WINDOW_BORDER_OUTLINE_WIDTH = 10

pygame.display.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warzone Loadout App")

HOME_SCREEN_IMAGE = pygame.image.load(os.path.join("images", "home_screen.jpg"))

MW_BUTTON_IMAGE = pygame.image.load(os.path.join("images", "modern_warfare_button.png"))
CW_BUTTON_IMAGE = pygame.image.load(os.path.join("images", "cold_war_button.png"))
VG_BUTTON_IMAGE = pygame.image.load(os.path.join("images", "vanguard_button.png"))
CREATE_LAODOUT_IMAGE = pygame.image.load(os.path.join("images", "create_loadout_button.png"))
HOME_BUTTON_IMAGE = pygame.image.load(os.path.join('images', 'home_button.png'))

MW_BUTTON = button.Button(340, 360, MW_BUTTON_IMAGE, 1.5)
CW_BUTTON = button.Button(680, 360, CW_BUTTON_IMAGE, 1.5)
VG_BUTTON = button.Button(340, 540, VG_BUTTON_IMAGE, 1.5)
CREATE_LOADOUT_BUTTON = button.Button(680, 540, CREATE_LAODOUT_IMAGE, 1.5)
HOME_BUTTON = button.Button(1190, 30, HOME_BUTTON_IMAGE, 0.75)


def draw_home_window():
    WIN.blit(HOME_SCREEN_IMAGE, (0, 0))
    MW_BUTTON.draw_image(WIN)
    CW_BUTTON.draw_image(WIN)
    VG_BUTTON.draw_image(WIN)
    CREATE_LOADOUT_BUTTON.draw_image(WIN)

    pygame.display.update()


def draw_mw_window():
    WIN.fill(WHITE)
    window_border = pygame.draw.rect(
        WIN, BLACK, [0, 0, WIDTH, HEIGHT], WINDOW_BORDER_OUTLINE_WIDTH
    )
    title_text = TITLE_FONT.render("MODERN FARFARE WEAPONS", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width() - 10) // 2, 30))
    HOME_BUTTON.draw_image(WIN)
    
    draw_labels()
    pygame.display.update()


def draw_cw_window():
    WIN.fill(WHITE)
    window_border = pygame.draw.rect(
        WIN, BLACK, [0, 0, WIDTH, HEIGHT], WINDOW_BORDER_OUTLINE_WIDTH
    )
    title_text = TITLE_FONT.render("COLD WAR WEAPONS", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width() - 10) // 2, 30))
    HOME_BUTTON.draw_image(WIN)

    draw_labels()
    pygame.display.update()


def draw_vg_window():
    WIN.fill(WHITE)
    window_border = pygame.draw.rect(
        WIN, BLACK, [0, 0, WIDTH, HEIGHT], WINDOW_BORDER_OUTLINE_WIDTH
    )
    title_text = TITLE_FONT.render("VANGUARD WEAPONS", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width() - 10) // 2, 30))
    HOME_BUTTON.draw_image(WIN)

    draw_labels()
    pygame.display.update()

def draw_create_loadout_window():
    WIN.fill(WHITE)
    window_border = pygame.draw.rect(
        WIN, BLACK, [0, 0, WIDTH, HEIGHT], WINDOW_BORDER_OUTLINE_WIDTH
    )
    title_text = TITLE_FONT.render("CREATE LOADOUT", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width() - 10) // 2, 30))
    HOME_BUTTON.draw_image(WIN)

    draw_labels()
    pygame.display.update()

    pygame.display.update()    

def draw_labels():
    labels_list = [
        "ars",
        "smgs",
        "shotguns",
        "lmgs",
        "marksman_rifle",
        "sniper_rifle",
        "handgun",
        "melee"
    ]

    width_list = [0]
    total_width = 0

    for text in labels_list:
        text = LABEL_FONT.render(text.upper(), True, BLACK)
        text_width = text.get_width()
        width_list.append(text_width)
        total_width += text_width
    
    starting_pos = (WIDTH - (WINDOW_BORDER_OUTLINE_WIDTH * 2) - total_width - ((len(width_list) - 2) * 50)) // 2

    for i, label in enumerate(labels_list):
        label = LABEL_FONT.render(label.upper(), True, BLACK)
        width_sum = sum(width_list[0:i+1])
        x_pos = starting_pos + width_sum + (i * 50)
        WIN.blit(label, (x_pos, 85))


def main():

    while True:
        game_state.state_manager()
        # draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
