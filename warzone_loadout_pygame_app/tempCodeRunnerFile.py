from functools import total_ordering
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
            if MW_BUTTON.draw(WIN) == True:
                self.state = "mw_screen"

        draw_home_window()

    def mw_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_mw_window()

    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        if self.state == "mw_screen":
            self.mw_screen()


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

MW_BUTTON = button.Button(510, 300, MW_BUTTON_IMAGE, 1.5)
CW_BUTTON = button.Button(510, 440, CW_BUTTON_IMAGE, 1.5)
VG_BUTTON = button.Button(510, 580, VG_BUTTON_IMAGE, 1.5)


def draw_home_window():
    WIN.blit(HOME_SCREEN_IMAGE, (0, 0))
    MW_BUTTON.draw(WIN)
    CW_BUTTON.draw(WIN)
    VG_BUTTON.draw(WIN)
    pygame.display.update()


def draw_mw_window():
    WIN.fill(WHITE)
    window_border = pygame.draw.rect(
        WIN, BLACK, [0, 0, WIDTH, HEIGHT], WINDOW_BORDER_OUTLINE_WIDTH
    )
    title_text = TITLE_FONT.render("MODERN FARFARE WEAPONS", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width() - 10) // 2, 30))
    # ars_label = LABEL_FONT.render("ARs", True, BLACK)
    # WIN.blit(ars_label, (100, 75))
    draw_labels()
    pygame.display.update()


def draw_cw_window():
    print()


def draw_vg_window():
    print()


def draw_labels():
    labels_list = [
        "ars",
        "smgs",
        "shotguns",
        "lmgs",
        "marksman_rifle",
        "sniper_rifle",
        "handgun",
        "melee",
    ]

    ars_label = LABEL_FONT.render('ARS', True, BLACK)
    smgs_label = LABEL_FONT.render('SMGS', True, BLACK)
    shotguns_label = LABEL_FONT.render('SHOTGUNS', True, BLACK)
    lmgs_label = LABEL_FONT.render('LMGS', True, BLACK)
    marksman_rifle_label = LABEL_FONT.render('MARKSMAN RIFLE', True, BLACK)
    sniper_rifle_label = LABEL_FONT.render('SNIPER RIFLE', True, BLACK)
    handgun_label = LABEL_FONT.render('HANDGUN', True, BLACK)
    melee_label = LABEL_FONT.render('MELEE', True, BLACK)

    WIN.blit(ars_label, (69, 75))
    WIN.blit(smgs_label, (161, 75))
    WIN.blit(shotguns_label, (273, 75))
    WIN.blit(lmgs_label, (438, 75))
    WIN.blit(marksman_rifle_label, (548, 75))
    WIN.blit(sniper_rifle_label, (783, 75))
    WIN.blit(handgun_label, (971, 75))
    WIN.blit(melee_label, (1123, 75))
    


def main():

    while True:
        game_state.state_manager()
        # draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
