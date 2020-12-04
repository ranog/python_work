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

HISTÓRICO
    20200312: João Paulo, dezembro de 2020.
        - Criando uma classe de configurações (pg 284-285).

------------------------------------------------------------------------
"""


class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
    Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
