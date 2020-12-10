#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    personagem_do_jogo.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x personagem_do_jogo.py
    $ ./personagem_do_jogo.py
    --- Abre uma tela preta de 1200 X 600 pixels. ---

------------------------------------------------------------------------

DESCRIÇÃO
    12.2 – Personagem do jogo: Encontre uma imagem de bitmap de um
    personagem de jogo que você goste ou converta uma imagem em um
    bitmap.
    Crie uma classe que desenhe o personagem no centro da tela e faça a
    cor de fundo da imagem coincidir com a cor de fundo da tela ou
    vice-versa.

------------------------------------------------------------------------

HISTÓRICO
    20201012: João Paulo, dezembro de 2020.
        - 12.2 – Personagem do jogo (pg 291).

------------------------------------------------------------------------
"""


import pygame

import game_functions as gf
from settings import Settings
from personagem import Personagem


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    # Instância da classe Settings do módulo settings.py.
    ai_settings = Settings()

    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Personagens")

    # Cria uma espaçonave
    personagem = Personagem(screen)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, personagem)


run_game()
