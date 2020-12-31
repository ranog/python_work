#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
        star.py - Criando a classe Star

------------------------------------------------------------------------

SINOPSES
        from star import Star

------------------------------------------------------------------------

DESCRIÇÃO
        13.1 – Estrelas: Encontre uma imagem de uma estrela. Faça uma
        grade de estrelas aparecer na tela.

------------------------------------------------------------------------

HISTÓRICO
        20202912: João Paulo, dezembro de 2020.
            - 13.1 - Estrelas (pg 320).

------------------------------------------------------------------------
"""


import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Uma classe que representa uma única estrela."""

    def __init__(self, ai_settings, screen):
        """Inicializa a estrela e define sua posição inicial."""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da estrela e define seu atributo rect.
        self.image = pygame.image.load('images/star-2402083_640.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova estrela próximo à parte superior esquerda
        # da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da estrela.
        self.x = float(self.rect.x)


    def blitme(self):
        """Desenha a estrela em sua posição atual."""
        self.screen.blit(self.image, self.rect)
