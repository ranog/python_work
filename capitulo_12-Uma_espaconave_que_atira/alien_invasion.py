#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    alien_invasion.py - Criando uma janela do Pygame e respondendo às
    entradas do usuário.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x alien_invasion.py
    $ ./alien_invasion.py
    --- Aparece uma tela preta de 1200 X 600 pixels. ---

------------------------------------------------------------------------

DESCRIÇÃO
    Inicialmente importamos os módulos sys e pygame . O módulo pygame
    contém as funcionalidades necessárias para criar um jogo. Usaremos o
    módulo sys para sair do jogo quando o usuário desistir.
    A Invasão Alienígena começa com a função run_game() . A linha
    pygame.init() inicializa as configurações de segundo plano de que o
    Pygame precisa para funcionar de forma apropriada. Chamamos
    pygame.display.set_mode() para criar uma janela de exibição chamada
    screen , na qual desenharemos todos os elementos gráficos do jogo. O
    argumento (1200, 600) é uma tupla que define as dimensões da janela
    do jogo. Ao passar essas dimensões para pygame.display.set_mode(),
    criamos uma janela de jogo com 1200 pixels de largura por 600 pixels
    de altura. (Esses valores podem ser ajustados de acordo com o
    tamanho de seu display.) O objeto screen é chamado de superfície.
    Uma superfície no Pygame é uma parte da tela em que exibimos um
    elemento do jogo.
    Cada elemento do jogo, por exemplo, os alienígenas ou a espaçonave,
    é uma superfície. A superfície devolvida por display.set_mode()
    representa a janela inteira do jogo. Quando ativamos o laço de
    animação do jogo, essa superfície é automaticamente redesenhada a
    cada passagem pelo laço.
    O jogo é controlado por um laço while que contém um laço de eventos
    e o código que administra as atualizações de tela. Um evento é uma
    ação realizada pelo usuário enquanto joga, por exemplo, pressionar
    uma tecla ou mover o mouse. Para fazer nosso programa responder aos
    eventos, escreveremos um laço de eventos para ouvir um evento e
    executar uma tarefa apropriada de acordo com o tipo de evento
    ocorrido. O laço for é um laço de eventos.
    Para acessar os eventos detectados pelo Pygame, usaremos
    pygame.event.get() . Qualquer evento de teclado ou de mouse fará o
    laço for executar. No laço, escreveremos uma série de instruções if
    para detectar e responder a eventos específicos. Por exemplo, quando
    o jogador clicar no botão de fechamento da janela do jogo, um evento
    pygame.QUIT será detectado e chamaremos sys.exit() para sair do
    jogo.
    A chamada a pygame.display.flip() diz ao Pygame para deixar visível
    a janela mais recente. Nesse caso, uma tela vazia será desenhada
    sempre que passarmos pelo laço while para apagar a tela antiga, de
    modo que apenas a nova janela esteja visível. Quando movermos
    elementos do jogo pela tela, pygame.display.flip() atualizará
    continuamente o display para mostrar as novas posições dos elementos
    e ocultar as posições anteriores, criando a ilusão de um movimento
    suave.
    A última linha nessa estrutura básica de jogo chama run_game() , que
    inicializa o jogo e o laço principal. Execute esse código agora e
    você verá uma janela vazia do Pygame.

------------------------------------------------------------------------

HISTÓRICO
    20200112: João Paulo, dezembro de 2020.
        - Criando uma janela do Pygame e respondendo às entradas do
        usuário (pg 282-283).

    20200212: João Paulo, dezembro de 2020.
        - Arrumando a indentação da DESCRIÇÃO.

------------------------------------------------------------------------

"""


import sys
import pygame


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()

