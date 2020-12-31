#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    star_functions.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    import star_functions as sf

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


import sys
import pygame
from random import randint

from star import Star


def check_events(ai_settings, screen):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, stars):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)

    stars.draw(screen)

    # Deixa a tela mais recente visível
    pygame.display.flip()


def get_number_stars_x(ai_settings, star_width):
    """Determina o número de estrelas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - star_width
    number_stars_x = int(available_space_x / star_width)
    return number_stars_x


def get_number_rows(ai_settings, star_height):
    """Determina o número de linhas com estrelas que cabem na
    tela."""
    available_space_y = (ai_settings.screen_height -  star_height)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows


def create_star(ai_settings, screen, stars, star_number, row_number):
    """Cria uma estrela e a posiciona na linha."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)


def create_stars(ai_settings, screen, stars):
    """Cria as estrelas."""

    # Cria uma estrela e calcula o número de estrelas em uma linha.
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    # Cria todas as estrelas.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):

            star_number = int(star_number)
            row_number = int(row_number)

            star = randint(0, star_number)
            row = randint(0, row_number)

            create_star(ai_settings, screen, stars, star, row)
