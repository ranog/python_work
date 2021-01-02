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

    O código de update_bullets() é removido de alien_invasion.py e
    colado no novo arquivo; o único parâmetro necessário é o grupo
    bullets.

------------------------------------------------------------------------

    A função fire_bullet() simplesmente contém o código usado para
    disparar um projétil quando a barra de espaço for pressionada; além
    disso, acrescentamos uma chamada a fire_bullet() em
    check_keydown_events() quando isso ocorrer.

------------------------------------------------------------------------

    Em check_keydown_events(), acrescentamos um novo bloco que finaliza
    o jogo quando Q é pressionado.

    É uma alteração razoavelmente segura, pois a tecla Q está longe das
    teclas de direção e da barra de espaço, portanto é improvável que o
    jogador pressione essa tecla por acidente e saia do jogo.

    Agora, ao testar, você poderá pressionar Q para encerrar o jogo, em
    vez de usar o seu mouse para fechar a janela.

------------------------------------------------------------------------

    Desenhamos o alienígena na tela depois que a espaçonave e os
    projéteis foram desenhados para que os alienígenas estejam na camada
    superior da tela.

------------------------------------------------------------------------

    Quando draw() é chamado em um grupo, o Pygame desenha
    automaticamente cada elemento do grupo na posição definida pelo seu
    atributo rect. Nesse caso, aliens.draw(screen) desenhará cada
    alienígena do grupo na tela.

------------------------------------------------------------------------

    Já analisamos a maior parte desse código. Precisamos conhecer a
    largura e a altura do alienígena para posicioná-los, portanto
    criamos um alienígena antes de fazer os cálculos.

    Esse alienígena não fará parte da frota, assim, não o adicione ao
    grupo aliens.

    Adquirimos a largura do alienígena a partir de seu atributo rect e
    armazenamos esse valor em alien_width; desse modo não precisaremos
    trabalhar com o atributo rect.

    Calculamos o espaço horizontal disponível para os alienígenas e o
    número de alienígenas que cabem nesse espaço.

    A única mudança aqui em relação às nossas fórmulas originais está no
    uso de int() para garantir que teremos um número inteiro de
    alienígenas, pois não queremos criar alienígenas parciais, e a
    função range() precisa de um inteiro.

    A função int() ignora a parte decimal de um número, fazendo o seu
    arredondamento para baixo (Isso é útil porque preferimos ter um
    pouco de espaço extra em cada linha a ter uma linha excessivamente
    congestionada).

    A seguir, defina um laço que conte de 0 até o número de alienígenas
    que devemos criar.

    No corpo principal do laço, crie um novo alienígena e então defina o
    valor de sua coordenada x para posicioná-lo na linha.

    Cada alienígena é inserido à direita, com um espaçamento
    correspondente à largura de um alienígena, a partir da margem
    esquerda.

    Em seguida, multiplicamos a largura do alienígena por dois para
    levar em consideração o espaço ocupado por cada alienígena,
    incluindo o espaço vazio à sua direita, e multiplicamos esse valor
    pela posição do alienígena na linha.

    Então adicionamos cada novo alienígena ao grupo aliens.

------------------------------------------------------------------------

    O corpo de get_number_aliens_x() está exatamente como era em
    create_fleet().

    O corpo de create_alien() também não mudou em relação a
    create_fleet(), exceto que usamos o alienígena que acabou de ser
    criado para obter a sua largura.

    Substituímos o código para determinar o espaçamento horizontal por
    uma chamada a get_number_aliens_x() e removemos a linha que
    referenciava alien_width, pois isso é tratado agora em
    create_alien().

    Chamamos create_alien().

    Essa refatoração facilitará o acréscimo de novas linha e a criação
    de uma frota completa.

------------------------------------------------------------------------

    Para calcular o número de linhas que cabem na tela, colocamos nossos
    cálculos de available_space_y e de number_rows na
    função get_number_rows(), que é semelhante a get_number_aliens_x().

    O cálculo está entre parênteses para que o resultado possa ser
    separado em duas linhas, o que resulta em linhas de 79 caracteres ou
    menos, conforme recomendado.

    Usamos int() porque não queremos criar uma linha parcial de
    alienígenas.

    Para criar várias linhas, usamos dois laços aninhados: um laço
    externo e outro interno.

    O laço interno cria os alienígenas em uma linha.

    O laço externo conta de 0 até o número de linhas que queremos;
    Python usará o código para criar uma única linha e repeti-la pelo
    número de vezes em number_rows.

    Para aninhar os laços, escreva o novo laço for e indente o código
    que você deseja repetir.

    Agora, ao chamar create_alien() , incluímos um argumento para o
    número da linha para que cada linha possa ser colocada cada vez mais
    para baixo na tela.

    A definição de create_alien() exige um parâmetro para armazenar o
    número da linha.

    Em create_alien() mudamos o valor da coordenada y de um alienígena
    quando ele não estiver na primeira linha, começando com a altura de
    um alienígena para criar um espaço vazio na parte superior da tela.

    Cada linha está separada da linha anterior pela altura de dois
    alienígenas, portanto multiplicamos a altura do alienígena por dois
    e então pelo número da linha.

    O número da primeira linha é 0, assim o posicionamento vertical da
    primeira linha não muda.

    Todas as linhas subsequentes são colocadas cada vez mais para baixo
    na tela.

------------------------------------------------------------------------

    Usamos o método update() no grupo aliens, o que faz o método
    update() de cada alienígena ser chamado automaticamente.

------------------------------------------------------------------------

    Em check_fleet_edges() percorremos a frota com um laço e chamamos
    check_edges() em cada alienígena.

    Se check_edges() devolver True, saberemos que um alienígena está em
    uma borda e toda a frota deverá mudar de direção, portanto chamamos
    change_fleet_direction() e saímos do laço.

    Em change_fleet_direction() percorremos todos os alienígenas com um
    laço e fazemos cada um deles descer na tela usando a configuração
    fleet_drop_speed; então alteramos o valor de fleet_direction
    multiplicando seu valor atual por -1.

    Modificamos a função update_aliens() a fim de determinar se algum
    alienígena está em uma das bordas chamando check_fleet_edges().

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

    20202812: João Paulo, dezembro de 2020.
        - Criando a função update_bullets (pg 306).
        - Criando a função fire_bullet() (pg 306-307).
        - Revisando o seu projeto (pg 310-311).

    20202912: João Paulo, dezembro de 2020.
        - Fazendo o alienígena aparecer na tela (pg 313).
        - Criando linhas de alienígenas (pg 314-315).
        - Criando a frota (pg 315-317).

    20203012: João Paulo, dezembro de 2020.
        - Refatorando create_fleet() (pg 317-318).
        - Adicionando linhas (pg 318-320).

    20210101: João Paulo, janeiro de 2021.
        - Movendo os alienígenas para a direita (pg 321).

    20200201: João Paulo, janeiro de 2021.
        - Fazendo a frota descer e mudando a direção (pg 323-324).

------------------------------------------------------------------------
"""


import sys
import pygame


from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Dispara um projétil se o limite ainda não foi alcançado. """

    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Responde a pressionamentos de tecla. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """ Responde a solturas de tecla. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Responde a eventos de pressionamento de teclas e de mouse. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Atualiza as imagens na tela e alterna para a nova tela. """

    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos
    # alienígenas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Deixa a tela mais recente visível
    pygame.display.flip()


def update_bullets(bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis
    antigos. """

    # Atualiza as posições dos projéteis.
    bullets.update()

    # Livra-se dos projéteis que desapareceram.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """ Determina o número de alienígenas que cabem em uma linha. """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determina o número de linhas com alienígenas que cabem na
    tela. """
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Cria um alienígena e o posiciona na linha. """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Cria uma frota completa de alienígenas. """

    # Cria um alienígena e calcula o número de alienígenas em uma linha.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # Cria a frota de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ai_settings, aliens):
    """ Faz toda a frota descer e muda a sua direção. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """ Responde apropriadamente se algum alienígena alcançou uma
    borda. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def update_aliens(ai_settings, aliens):
    """ Verifica se a frota está em uma das bordas e então atualiza as
    posições de todos os alienígenas da frota. """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
