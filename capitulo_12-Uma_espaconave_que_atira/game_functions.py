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

    Fornecemos um parâmetro ship à função check_events() porque a nave
    deve se deslocar para a direita quando a tecla para a direita for
    pressionada. Em check_events(), acrescentamos um bloco elif no laço
    de eventos para responder quando o Pygame detectar um evento
    KEYDOWN.
    Verificamos se a tecla pressionada é a seta para a direita
    (pygame.K_RIGHT) lendo o atributo event.key. Se a seta para a
    direita foi pressionada, movemos a espaçonave para a direita
    incrementando o valor de ship.rect.centerx de 1.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - Função check_events() (pg 289-290).
        - Função update_screen() (pg 290-291).

    20201112: João Paulo, dezembro de 2020.
        - Respondendo a um pressionamento de tecla (pg 291-292).

------------------------------------------------------------------------
"""


import sys
import pygame


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move a espaçonave para a direita
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
