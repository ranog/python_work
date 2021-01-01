#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
        alien.py - Criando a classe Alien

------------------------------------------------------------------------

SINOPSES
        from alien import Alien

------------------------------------------------------------------------

DESCRIÇÃO
        A maior parte dessa classe é semelhante à classe Ship, exceto
        pelo posicionamento do alienígena.

        Posicionaremos inicialmente cada alienígena próximo ao canto
        superior esquerdo da tela, colocando um espaço à esquerda que
        seja igual à largura do alienígena e um espaço acima dele
        correspondente à sua altura.

------------------------------------------------------------------------

        Sempre que atualizarmos a posição de um alienígena, ele será
        movido para a direita de acordo com o valor armazenado em
        alien_speed_factor.

        Controlamos a posição exata do alienígena com o atributo self.x,
        que é capaz de armazenar valores decimais. Então usamos o valor
        de self.x para atualizar a posição do rect do alienígena.

------------------------------------------------------------------------

HISTÓRICO
        20202912: João Paulo, dezembro de 2020.
            - Criando a classe Alien (pg 312).

        20210101: João Paulo, janeiro de 2021.
            - Movendo os alienígenas para a direita (pg 321).

------------------------------------------------------------------------
"""


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda
        # da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena.
        self.x = float(self.rect.x)


    def update(self):
        """Move o alienígena para a direita."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x


    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)
