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

    O grupo bullets é passado para check_keydown_events().

    Quando o jogador pressiona a barra de espaço, criamos um novo
    projétil (uma instância de Bullet que chamamos de new_bullet) e o
    adicionamos ao grupo bullets usando o método add(); o código
    bullets.add(new_bullet) armazena o novo projétil no grupo bullets.

    Precisamos acrescentar bullets como parâmetro na definição de
    check_events() e passar bullets como argumento na chamada a
    check_keydown_events() também.

    Passamos o parâmetro bullets para update_screen(), que desenha os
    projéteis na tela.

    O método bullets.sprites() devolve uma lista de todos os sprites do
    grupo bullets.

    Para desenhar todos os projéteis disparados na tela, percorremos os
    sprites em bullets com um laço e chamamos draw_bullet() em cada um.

------------------------------------------------------------------------

    Quando a barra de espaço é pressionada, verificamos o tamanho de
    bullets.

    Se len(bullets) for menor que três, criaremos um novo projétil.

    No entanto, se já houver três projéteis ativos, nada acontecerá
    quando a barra de espaço for pressionada.

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

    20202712: João Paulo, dezembro de 2020.
        - Disparando os projéteis (pg 303-304).
        - Limitando o número de projéteis (pg 305-306).

------------------------------------------------------------------------
"""


import sys
import pygame


from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos
    # alienígenas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
