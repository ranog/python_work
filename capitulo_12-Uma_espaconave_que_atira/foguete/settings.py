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

    Definimos o valor inicial de ship_speed_factor com 1.5 .

    Quando quisermos mover a espaçonave, ajustaremos sua posição em 1,5
    pixel, e não em 1 pixel.

    Usamos valores decimais para a configuração da velocidade para que
    possamos ter um controle mais preciso da velocidade da espaçonave
    quando aumentarmos o ritmo do jogo mais tarde.

------------------------------------------------------------------------

HISTÓRICO
    20200312: João Paulo, dezembro de 2020.
        - Criando uma classe de configurações (pg 284-285).

    20202412: João Paulo, dezembro de 2020.
        - Ajustando a velocidade da espaçonave (pg 295-297).

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

        # Configurações da espaçonave
        self.space_shuttle_speed_factor = 1.5
