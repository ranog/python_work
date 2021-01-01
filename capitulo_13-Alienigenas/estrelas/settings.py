#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    settings.py - Criando uma classe de configurações.

------------------------------------------------------------------------

SINOPSES
    from settings import Settings

------------------------------------------------------------------------

DESCRIÇÃO
    Armazena todas as configurações em um só lugar.

------------------------------------------------------------------------

    13.1 – Estrelas: Encontre uma imagem de uma estrela. Faça uma grade
    de estrelas aparecer na tela.

    13.2 – Estrelas melhoradas: Você pode criar um padrão mais realista
    de estrelas introduzindo uma aleatoriedade ao posicionar cada
    estrela. Lembre-se de que um número aleatório pode ser obtido assim:
    from random import randint random_number = randint(-10,10) Esse
    código devolve um inteiro aleatório entre −10 e 10. Usando o seu
    código do Exercício 13.1, ajuste a posição de cada estrela de acordo
    com um valor aleatório.

------------------------------------------------------------------------

HISTÓRICO
    20200312: João Paulo, dezembro de 2020.
        - Criando uma classe de configurações (pg 284-285).

    20203112: João Paulo, dezembro de 2020.
        - 13.1 – Estrelas (pg 320).
        - 13.2 – Estrelas melhoradas (pg 320).

------------------------------------------------------------------------
"""


class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
    Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela.
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
