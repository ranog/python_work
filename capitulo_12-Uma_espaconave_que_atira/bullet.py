#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
        bullet.py - Criando a classe Bullet.

------------------------------------------------------------------------

SINOPSES

------------------------------------------------------------------------

DESCRIÇÃO
        A classe Bullet herda de Sprite, que importamos do módulo
        pygame.sprite.

        Ao usar sprites, podemos agrupar elementos relacionados no jogo
        e atuar em todos os elementos agrupados de uma só vez.

        Para criar uma instância de um projétil, __init__() precisa das
        instâncias ai_settings, screen e ship; além disso, chamamos
        super() para herdar de modo apropriado de Sprite.

        NOTA
            A chamada a super(Bullet, self).__init__() usa a sintaxe de
            Python 2.7.

            Essa sintaxe funciona em Python 3 também; de modo
            alternativo, essa chamada pode ser feita de forma mais
            simples como super().__init__().

        Criamos o atributo rect do projétil.

        O projétil não está baseado em uma imagem, portanto precisamos
        criar um retângulo do zero usando a classe pygame.Rect().

        Essa classe exige as coordenadas x e y do canto superior
        esquerdo do rect, além de sua largura e sua altura.

        Inicializamos o rect em (0, 0), mas ele será movido para o local
        correto nas duas próximas linhas porque a posição do projétil
        depende da posição da espaçonave.

        Os valores da largura e da altura do projétil são obtidos dos
        valores armazenados em ai_settings.

        Definimos o centerx do projétil para que seja igual ao
        rect.centerx da espaçonave.

        O projétil deve emergir da parte superior da espaçonave,
        portanto definimos o rect do projétil para que sua parte
        superior coincida com a parte superior do rect da espaçonave,
        fazendo parecer que o projétil foi disparado da espaçonave.

        Armazenamos um valor decimal para a coordenada y do projétil
        para que possamos fazer ajustes mais precisos em sua velocidade.

        Armazenamos a cor e as configurações de velocidade do projétil
        em self.color e em self.speed_factor.

        O método update() administra a posição do projétil.

        Quando um projétil é disparado, ele se move para cima na tela, o
        que corresponde a um decréscimo no valor da coordenada y;
        portanto, para atualizar a posição, subtraímos de self.y a
        quantidade armazenada em self.speed_factor.

        Então usamos o valor de self.y para definir o valor de
        self.rect.y.

        O atributo speed_factor nos permite aumentar a velocidade dos
        projéteis à medida que o jogo progredir ou conforme for
        necessário para melhor ajustar o comportamento do jogo.

        Depois que o projétil é disparado, o valor de sua coordenada x
        não muda, portanto ele só se deslocará na vertical, em linha
        reta.

        Se quisermos desenhar um projétil, chamaremos draw_bullet().

        A função draw.rect() preenche a parte da tela definida pelo rect
        do projétil com a cor armazenada em self.color.

------------------------------------------------------------------------

HISTÓRICO
        20202612: João Paulo, dezembro de 2020.
            - Criando a classe Bullet (pg 300-301).

------------------------------------------------------------------------
"""


import  pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela
    espaçonave."""
    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto para o projétil na posição atual da
        espaçonave."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Cria um retângulo para o projétil em (0, 0) e, em seguida,
        # define a posição correta.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posição do projétil como um valor decimal.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil
        self.y -= self.speed_factor

        # Atualiza a posição de rect
        self.rect.y = self.y


    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
