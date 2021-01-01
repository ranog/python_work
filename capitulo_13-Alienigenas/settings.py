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

    As configurações criam projéteis cinza-escuros, com largura de 3
    pixels e altura de 15 pixels. Os projéteis se deslocarão de modo um
    pouco mais lento que a espaçonave.

------------------------------------------------------------------------

    A configuração fleet_drop_speed controla a velocidade com que a
    frota desce na tela sempre que um alienígena alcançar uma das
    bordas.

    É conveniente separar essa velocidade da velocidade horizontal dos
    alienígenas para que você possa ajustar as duas velocidades de modo
    independente.

    Para implementar a configuração fleet_direction poderíamos ter usado
    um valor textual, por exemplo, 'left' ou 'right' , mas acabaríamos
    com instruções if-elif para testar a direção da frota.

    Em vez disso, como temos apenas duas direções, vamos usar os valores
    1 e -1 e alternar entre eles sempre que a frota mudar de direção.

    (Usar números também faz sentido porque movimentar-se para a direita
    envolve somar um valor à coordenada x de cada alienígena, enquanto
    movimentar-se para a esquerda envolve fazer uma subtração no valor
    da coordenada x de cada alienígena.)

------------------------------------------------------------------------

HISTÓRICO
    20200312: João Paulo, dezembro de 2020.
        - Criando uma classe de configurações (pg 284-285).

    20202412: João Paulo, dezembro de 2020.
        - Ajustando a velocidade da espaçonave (pg 295-297).

    20202612: João Paulo, dezembro de 2020.
        - Criando a classe Bullet (pg 300-301).

    20202712: João Paulo, dezembro de 2020.
        - Limitando o número de projéteis (pg 305-306).

    20210101: João Paulo, janeiro de 2021.
        - Movendo os alienígenas para a direita (pg 321).
        - Criando configurações para a direção da frota (pg 322).

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
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave.
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # Essa instrução limita o jogador a três projéteis ao mesmo
        # tempo.
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa
        # a esquerda.
        self.fleet_direction = 1
