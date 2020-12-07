#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    ship.py - Criando a classe Ship.

------------------------------------------------------------------------

SINOPSES
    from ship import Ship

------------------------------------------------------------------------

DESCRIÇÃO
    Inicialmente importamos o módulo pygame. O método __init__() de Ship
    aceita dois parâmetros: a referência self e screen, que é a tela em
    que desenharemos a espaçonave.

    Para carregar a imagem, chamamos pygame.image.load(). Essa função
    devolve uma superfície que representa a espaçonave; essa informação
    é armazenada em self.image.

    Depois que a imagem é carregada, usamos get_rect() para acessar o
    atributo rect da superfície. Um motivo para o Pygame ser tão
    eficiente é que ele permite tratar elementos do jogo como retângulos
    (rects), mesmo que eles não tenham exatamente o formato de um
    retângulo.

    Tratar um elemento como um retângulo é eficaz, pois os retângulos
    são formas geométricas simples. Essa abordagem geralmente funciona
    bem, a ponto de ninguém que esteja jogando perceba que não estamos
    trabalhando com a forma exata de cada elemento do jogo.

    Quando trabalhamos com um objeto rect, podemos usar as coordenadas x
    e y das bordas superior, inferior, esquerda e direita do retângulo,
    assim como o centro. Podemos definir qualquer um desses valores a
    fim de determinar a posição atual do retângulo.

    Quando um elemento do jogo for centralizado, trabalhe com os
    atributos center, centerx ou centery de um retângulo. Quando
    trabalhar com uma borda da tela, use os atributos top, bottom, left
    ou right.

    Quando ajustar a posição horizontal ou vertical do retângulo, você
    pode simplesmente usar os atributos x e y, que correspondem às
    coordenadas x e y de seu canto superior esquerdo. Esses atributos
    evitam que você precise fazer cálculos que os desenvolvedores de
    jogos tinham que efetuar manualmente no passado, e você perceberá
    que usará esses atributos com frequência.

    NOTA
    No Pygame, a origem (0, 0) está no canto superior esquerdo da tela,
    e as coordenadas aumentam à medida que você descer e se deslocar
    para a direita. Em uma tela de 1200 por 800, a origem está no canto
    superior esquerdo, e o canto inferior direito tem as coordenadas
    (1200, 800).

    Posicionaremos a espaçonave na parte inferior central da tela. Para
    isso, inicialmente armazene o retângulo da tela em self.screen_rect
    e, em seguida, faça o valor de self.rect.centerx (a coordenada x do
    centro da espaçonave) coincidir com o atributo centerx do retângulo
    da tela.

    Faça com que o valor de self.rect.bottom (a coordenada y da parte
    inferior da espaçonave) seja igual ao valor do atributo bottom do
    retângulo da tela. O Pygame usará esses atributos rect para
    posicionar a imagem da espaçonave de modo que ela esteja
    centralizada horizontalmente e alinhada com a parte inferior da
    tela.

    Definimos o método blitme(), que desenhará a imagem na tela na
    posição especificada por self.rect.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - Criando a classe Ship (pg 286-288).

------------------------------------------------------------------------
"""


import pygame


class Ship():
    """Administra a maior parte do comportamento da espaçonave do
    jogador."""

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)
