#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    ceu_azul.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x ceu_azul.py
    $ ./ceu_azul.py

------------------------------------------------------------------------

DESCRIÇÃO
    12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo
    azul.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - 12.1 – Céu azul (pg 291).

------------------------------------------------------------------------
"""

import pygame
import sys

def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("12.1 - Céu azul")
    # Define a cor de fundo.
    bg_color = (0, 0, 255)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        # Deixa a tela mais recente visível.
        pygame.display.flip()


run_game()
