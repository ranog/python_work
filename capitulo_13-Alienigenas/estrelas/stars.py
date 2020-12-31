#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
        stars.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
        $ chmod +x stars.py
        $ ./stars.py
        --- Abre uma tela preta de 1200 X 600 pixels com estrelas
        amarelas. ---

------------------------------------------------------------------------

DESCRIÇÃO
        13.1 – Estrelas: Encontre uma imagem de uma estrela. Faça uma
        grade de estrelas aparecer na tela.

------------------------------------------------------------------------

HISTÓRICO
        20203112: João Paulo, dezembro de 2020.
            - 13.1 – Estrelas (pg 320).

------------------------------------------------------------------------
"""


import pygame
from pygame.sprite import Group


import star_functions as sf
from settings import Settings


def run_game():
    # Inicializa o exercício e cria um objeto para a tela.
    pygame.init()

    # Instância da classe Settings do módulo settings.py.
    ai_settings = Settings()

    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    # Cria o grupo de estrelas.
    stars = Group()

    # Cria as estreals.
    sf.create_stars(ai_settings, screen, stars)

    # Inicia o laço principal do exercício.
    while True:
        sf.check_events(ai_settings, screen)
        sf.update_screen(ai_settings, screen, stars)


run_game()
