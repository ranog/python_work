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
    --- Abre uma tela preta de 1200 X 600 pixels. ---
    --- Abre uma tela cinza-claro de 1200 X 600 pixels. ---

------------------------------------------------------------------------

DESCRIÇÃO
    Inicialmente importamos os módulos sys e pygame. O módulo pygame
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
    tamanho de seu display - no livro é 1200 X 800).

    O objeto screen é chamado de superfície. Uma superfície no Pygame é
    uma parte da tela em que exibimos um elemento do jogo. Cada elemento
    do jogo, por exemplo, os alienígenas ou a espaçonave, é uma
    superfície. A superfície devolvida por display.set_mode() representa
    a janela inteira do jogo. Quando ativamos o laço de animação do
    jogo, essa superfície é automaticamente redesenhada a cada passagem
    pelo laço.

    O jogo é controlado por um laço while que contém um laço de eventos
    e o código que administra as atualizações de tela. Um evento é uma
    ação realizada pelo usuário enquanto joga, por exemplo, pressionar
    uma tecla ou mover o mouse. Para fazer nosso programa responder aos
    eventos, escreveremos um laço de eventos para ouvir um evento e
    executar uma tarefa apropriada de acordo com o tipo de evento
    ocorrido. O laço for é um laço de eventos.

    Para acessar os eventos detectados pelo Pygame, usaremos
    pygame.event.get(). Qualquer evento de teclado ou de mouse fará o
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

    Inicialmente criamos uma cor de fundo e a armazenamos em bg_color.
    Essa cor deve ser especificada apenas uma vez, portanto definimos
    seu valor antes de entrar no laço while principal.

    As cores no Pygame são especificadas como cores RGB: uma mistura de
    vermelho, verde e azul. O valor de cada cor varia de 0 a 255. A cor
    representada pelo valor (255, 0, 0) é vermelha, por (0, 255, 0) é
    verde e por (0, 0, 255) é azul. Podemos misturar valores RGB para
    criar 16 milhões de cores. A cor cujo valor é (230, 230, 230)
    mistura quantidades iguais de vermelho, azul e verde, produzindo uma
    cor de fundo cinza-claro.

    Preenchemos a tela com a cor de fundo usando o método screen.fill(),
    que aceita apenas um argumento: uma cor.

------------------------------------------------------------------------

    Importamos Settings no arquivo principal do programa e, em seguida,
    criamos uma instância de Settings e a armazenamos em ai_settings
    depois de fazer a chamada a pygame.init(). Quando criamos uma tela,
    usamos os atributos screen_width e screen_height de ai_settings e
    então usamos ai_settings também para acessar a cor de fundo quando
    preenchemos a tela

------------------------------------------------------------------------

    Importamos Ship e então criamos uma instância de Ship (chamada ship)
    depois que a tela foi criada. Essa operação deve estar antes do laço
    while principal para que uma nova instância da espaçonave não seja
    criada a cada passagem pelo laço. Desenhamos a espaçonave na tela
    chamando ship.blitme() depois de preencher a cor de fundo; assim a
    espaçonave aparecerá sobre essa cor

------------------------------------------------------------------------

    Não precisamos mais importar sys diretamente no arquivo principal do
    programa, pois ele é usado apenas no módulo game_functions agora.
    Atribuímos o alias gf ao módulo importado game_functions para
    simplificar.

------------------------------------------------------------------------

    Essas duas funções deixam o laço while mais simples e facilitará os
    desenvolvimentos futuros. Em vez de trabalhar em run_game(), podemos
    fazer a maior parte de nossas tarefas no módulo game_functions.

------------------------------------------------------------------------

    Devemos ver a nave mover-se para a direita em um pixel sempre que a
    seta para a direita for pressionada.

------------------------------------------------------------------------

    A posição da espaçonave será atualizada depois que verificarmos os
    eventos de teclado e antes de atualizarmos a tela.

    Isso permite que a posição da nave seja atualizada em resposta a uma
    entrada do jogador e garante que a posição atualizada seja usada
    quando a espaçonave for desenhada na tela.

    Ao executar alien_invasion.py e manter a seta para a direita
    pressionada, a espaçonave deverá mover-se continuamente para a
    direita até que a tecla seja solta.

------------------------------------------------------------------------

    Agora qualquer valor de ship_speed_faictor maior que um fará a
    espaçonave se deslocar mais rapidamente.

    Isso será útil para fazer com que a espaçonave responda rápido o
    suficiente para atingir os alienígenas, e nos permitirá mudar o
    ritmo do jogo à medida que o jogador fizer progressos no gameplay.

------------------------------------------------------------------------

    Importamos Group de pygame.sprite.

    Criamos uma instância de Group e a chamamos de bullets.

    Esse grupo é criado fora do laço while para que um novo grupo de
    projéteis não seja criado a cada ciclo do laço.

    NOTA
        Se você criar um grupo como esse dentro do laço, estará criando
        milhares de grupos de projéteis, e seu jogo provavelmente ficará
        muito lento.

        Se seu jogo travar, observe com atenção o que está acontecendo
        em seu laço while principal.

    Passamos bullets para check_events() e para update_screen().

    Teremos que trabalhar com bullets em check_events() quando a barra
    de espaço for pressionada, e precisaremos atualizar os projéteis
    desenhados na tela em update_screen().

    Quando chamamos update() em um grupo, ele chamará update()
    automaticamente para cada sprite do grupo.

    A linha bullets.update() chama bullet.update() para cada projétil
    que colocamos no grupo bullets.

------------------------------------------------------------------------

    Não devemos remover itens de uma lista ou de um grupo em um laço
    for, portanto precisamos usar uma cópia do grupo no laço.

    Utilizamos o método copy() para preparar o laço for, o que nos
    permite modificar bullets no laço.

    Verificamos cada projétil para ver se ele desapareceu por ter
    ultrapassado a parte superior da tela.

    Em caso afirmativo, o projétil é removido de bullets.

    Inserimos uma instrução print para mostrar quantos projéteis existem
    no momento no jogo e conferir se estão sendo apagados.

------------------------------------------------------------------------

    Criamos o programa de modo que o nosso laço principal contenha
    apenas um mínimo de código para que possamos ler rapidamente os
    nomes das funções e entender o que acontece no jogo.

    O laço principal verifica se há entradas do jogador e então atualiza
    a posição da espaçonave e de qualquer projétil que tenha sido
    disparado.

    Em seguida usamos as posições atualizadas para desenhar uma nova
    tela.

------------------------------------------------------------------------

HISTÓRICO
    20200112: João Paulo, dezembro de 2020.
        - Criando uma janela do Pygame e respondendo às entradas do
        usuário (pg 282-283).

    20200212: João Paulo, dezembro de 2020.
        - Arrumando a indentação da DESCRIÇÃO.

    20200312: João Paulo, dezembro de 2020.
        - Definindo a cor de fundo (pg 283-284).
        - Criando uma classe de configurações (pg 284-285).

    20200512: João Paulo, dezembro de 2020.
        - Desenhando a espaçonave na tela (pg 288).
        - Função check_events() (pg 289-290).
        - Função update_screen() (pg 290-291).

    20201212: João Paulo, dezembro de 2020.
        - Permitindo um movimento contínuo (pg 292-294).

    20202412: João Paulo, dezembro de 2020.
        - Ajustando a velocidade da espaçonave (pg 295-297).


    20202712: João Paulo, dezembro de 2020.
        - Armazenando projéteis em um grupo (pg 302).
        - Apagando projéteis antigos (pg 304-305).

    20202812: João Paulo, dezembro de 2020.
        - Criando a função update_bullets() (pg 306).

------------------------------------------------------------------------
"""


import pygame
from pygame.sprite import Group


import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela.
    pygame.init()

    # Instância da classe Settings do módulo settings.py.
    ai_settings = Settings()

    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave.
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis.
    bullets = Group()

    # Inicia o laço principal do jogo.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # 12.5 – Disparos laterais (pg 307).
        gf.update_bullets(bullets, ai_settings)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
