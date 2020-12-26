#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    game_functions.py - Função check_events().

------------------------------------------------------------------------

SINOPSES
    import game_functions as gf

------------------------------------------------------------------------

DESCRIÇÃO
    Esse módulo importa sys e pygame, usados no laço de verificação de
    eventos. A função não precisa de nenhum parâmetro no momento, e seu
    corpo foi copiado do laço de eventos em alien_invasion.py.

------------------------------------------------------------------------

    A nova função update_screen() aceita três parâmetros: ai_settings,
    screen e ship.

------------------------------------------------------------------------

    Fornecemos um parâmetro ship à função check_events() porque a nave
    deve se deslocar para a direita quando a tecla para a direita for
    pressionada. Em check_events(), acrescentamos um bloco elif no laço
    de eventos para responder quando o Pygame detectar um evento
    KEYDOWN.

    Verificamos se a tecla pressionada é a seta para a direita
    (pygame.K_RIGHT) lendo o atributo event.key. Se a seta para a
    direita foi pressionada, movemos a espaçonave para a direita
    incrementando o valor de ship.rect.centerx de 1.

------------------------------------------------------------------------

    Modificamos o modo como o jogo responde quando o jogador pressiona a
    seta para a direita; em vez de mudar a posição da espaçonave de
    forma direta, simplesmente definimos moving_right com True.

    Adicionamos um novo bloco elif que responde a eventos KEYUP.

    Quando o jogador soltar a tecla de seta para a direita (K_RIGHT),
    definiremos moving_right com False.

------------------------------------------------------------------------

    Se um evento KEYDOWN ocorrer para a tecla K_LEFT, definimos
    moving_left com True. Se um evento KEYUP ocorrer para a tecla
    K_LEFT, definimos moving_left com False. Podemos usar blocos elif
    nesse caso, pois cada evento está associado a apenas uma tecla. Se o
    jogador pressionar as duas teclas ao mesmo tempo, dois eventos
    diferentes serão detectados.

------------------------------------------------------------------------

    Criamos duas novas funções: check_keydown_events() e
    check_keyup_events().

    Cada uma delas precisa de um parâmetro event e de um parâmetro ship.

    Os corpos dessas duas funções foram copiados de check_events() e
    substituímos o código antigo por chamadas às novas funções.

    A função check_events() está mais simples agora, com uma estrutura
    de código mais limpa, o que facilitará o desenvolvimento de outras
    respostas a entradas do usuário.

------------------------------------------------------------------------

    12.3 – Foguete: Crie um jogo que comece com um foguete no centro da
    tela.

    Permita que o jogador mova o foguete para cima, para baixo, para a
    direita e para a esquerda usando as quatro teclas de direção.

    Garanta que o foguete não se desloque para além de qualquer borda da
    tela.

------------------------------------------------------------------------

HISTÓRICO
    20200512: João Paulo, dezembro de 2020.
        - Função check_events() (pg 289-290).
        - Função update_screen() (pg 290-291).

    20201112: João Paulo, dezembro de 2020.
        - Respondendo a um pressionamento de tecla (pg 291-292).

    20201212: João Paulo, dezembro de 2020.
        - Permitindo um movimento contínuo (pg 292-294).

    20201512: João Paulo, dezembro de 2020.
        - Movendo tanto para a esquerda quanto para a direita
         (pg 294-295).

    20202412: João Paulo, dezembro de 2020.
        - Refatorando check_events() (pg 297-298).

    20202612: João Paulo, dezembro de 2020.
        - 12.3 – Foguete (pg 299).

------------------------------------------------------------------------
"""


import sys
import pygame


def check_keydown_events(event, ship):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # XXX 12.3 – Foguete (pg 299):
    if event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    # XXX 12.3 – Foguete (pg 299)
    if event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
