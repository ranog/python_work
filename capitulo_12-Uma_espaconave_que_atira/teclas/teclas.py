#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    teclas.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x teclas.py
    $ ./teclas.py
    1073741916
    1073741919
    1073741921
    100
    102
    100
    121
    114
    ...

------------------------------------------------------------------------

DESCRIÇÃO
    12.4 – Teclas: Em um arquivo Pygame, crie uma tela vazia. No laço de
    eventos, exiba o atributo event.key sempre que o evento
    pygame.KEYDOWN for detectado.

    Execute o programa e pressione várias teclas para ver como o Pygame
    responde.

------------------------------------------------------------------------

HISTÓRICO
    20202612: João Paulo, dezembro de 2020.
        - 12.4 – Teclas (pg 299).

------------------------------------------------------------------------
"""

import pygame
import sys

def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("12.4 - Teclas")
    # Define a cor de fundo.
    bg_color = (255, 255, 255)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill(bg_color)
        # Deixa a tela mais recente visível.
        pygame.display.flip()


run_game()
