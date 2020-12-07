#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    game_functions.py - Função check_events().

------------------------------------------------------------------------

SINOPSES
    import game_functions as gf

------------------------------------------------------------------------

DESCRIÇÃO
    Esse módulo importa sys e pygame, usados no laço de verificação de
    eventos. A função não precisa de nenhum parâmetro no momento, e seu
    corpo foi copiado do laço de eventos em alien_invasion.py.

------------------------------------------------------------------------

    A nova função update_screen() aceita três parâmetros: ai_settings,
    screen e ship.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - Função check_events() (pg 289-290).
        - Função update_screen() (pg 290-291).

------------------------------------------------------------------------
"""


import sys
import pygame


def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
