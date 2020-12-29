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

    Adicionamos um atributo self.moving_right no método __init__() e o
    definimos com False inicialmente. Então acrescentamos update() , que
    move a espaçonave para a direita se a flag for True.

------------------------------------------------------------------------

    Em __init__(), acrescentamos uma flag self.moving_left. Em update()
    usamos dois blocos if separados em vez de utilizar um elif em
    update() para permitir que o valor rect.centerx da espaçonave seja
    incrementado e então decrementado se as duas teclas de direção forem
    mantidas pressionadas. Isso resulta na espaçonave parada. Se
    usássemos elif para o movimento à esquerda, a seta para a direita
    sempre teria prioridade. Fazer isso dessa maneira deixa os
    movimentos mais precisos ao alternamos o movimento da esquerda para
    a direita, quando o jogador poderia momentaneamente manter as duas
    teclas pressionadas.

------------------------------------------------------------------------

    Adicionamos ai_settings à lista de parâmetros de __init__() para que
    a espaçonave tenha acesso à sua configuração de velocidade.

    Então transformamos o parâmetro ai_settings em um atributo para que
    possamos usá-lo em update().

    Agora que estamos ajustando a posição da espaçonave em frações de um
    pixel, precisamos armazenar a posição em uma variável capaz de
    armazenar um valor decimal.

    Você pode usar um valor decimal para definir um atributo de rect,
    mas rect armazenará apenas a parte inteira desse valor.

    Para armazenar a posição da espaçonave de forma precisa, definimos
    um novo atributo self.center, capaz de armazenar valores decimais.

    Usamos a função float() para converter o valor de self.rect.centerx
    em um decimal e armazenamos esse valor em self.center.

    Agora, quando alterarmos a posição da espaçonave em update(), o
    valor de self.center será ajustado de acordo com a quantidade
    armazenada em ai_settings.ship_speed_factor.

    Depois que self.center é atualizado, usamos o novo valor para
    atualizar self.rect.centerx, que controla a posição da espaçonave.

    Somente a parte inteira de self.center será armazenada em
    self.rect.centerx, mas isso não é um problema para exibir a
    espaçonave.

------------------------------------------------------------------------

    Esse código verifica a posição da espaçonave antes de alterar o
    valor de self.center.

    O código self.rect.right devolve o valor da coordenada x da borda
    direita do rect da espaçonave.

    Se esse valor for menor que o valor devolvido por
    self.screen_rect.right, é sinal de que a espaçonave não alcançou a
    borda direita da tela.

    O mesmo vale para a borda esquerda: se o valor do lado esquerdo de
    rect for maior que zero, a espaçonave não atingiu a borda esquerda
    da tela.

    Isso garante que a espaçonave esteja dentro desses limites antes de
    ajustar o valor de self.center.

------------------------------------------------------------------------

    12.5 – Disparos laterais: Escreva um jogo que posicione uma
    espaçonave do lado esquerdo da tela e permita que o jogador a
    desloque para cima e para baixo.

    Faça a espaçonave disparar um projétil que se move para a direita da
    tela quando o jogador pressionar a barra de espaço.

    Garanta que os projéteis sejam apagados quando desaparecerem da tela.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - Criando a classe Ship (pg 286-288).

    20201212: João Paulo, dezembro de 2020.
        - Permitindo um movimento contínuo (pg 292-294).

    20201512: João Paulo, dezembro de 2020.
        - Movendo tanto para a esquerda quanto para a direita
        (pg 294-295).

    20202412: João Paulo, dezembro de 2020.
        - Ajustando a velocidade da espaçonave (pg 295-297).
        - Limitando o alcance da espaçonave (pg 297).

    20202812: João Paulo, dezembro de 2020.
        - 12.5 – Disparos laterais (pg 307).

------------------------------------------------------------------------
"""


import pygame


class Ship():
    """Administra a maior parte do comportamento da espaçonave do
    jogador."""


    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/fighter_30.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave no centro e do lado esquerdo da
        # tela.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centery)

        # Flag de movimento
        # 12.5 – Disparos laterais (pg 307).
        self.moving_top = False
        self.moving_bottom = False


    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de
        movimento."""
        # Atualiza o valor do centro da espaçonave, e não o retângulo.
        # 12.5 – Disparos laterais (pg 307).
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centery = self.center


    def blitme(self):
        """Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)
