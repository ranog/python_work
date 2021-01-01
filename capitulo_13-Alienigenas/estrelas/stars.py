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

        13.2 – Estrelas melhoradas: Você pode criar um padrão mais
        realista de estrelas introduzindo uma aleatoriedade ao
        posicionar cada estrela. Lembre-se de que um número aleatório
        pode ser obtido assim: from random import randint
        random_number = randint(-10,10) Esse código devolve um inteiro
        aleatório entre −10 e 10. Usando o seu código do Exercício 13.1,
        ajuste a posição de cada estrela de acordo com um valor
        aleatório.

------------------------------------------------------------------------

HISTÓRICO
        20203112: João Paulo, dezembro de 2020.
            - 13.1 – Estrelas (pg 320).
            - 13.2 – Estrelas melhoradas (pg 320).

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
