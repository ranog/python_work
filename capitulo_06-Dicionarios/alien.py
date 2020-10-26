#! /usr/bin/env python3

"""
NOME
    alien.py - Um dicionário simples

SINOPSES
    chmod +x alien.py
    ./alien.py
    green
    5

    - You just earned 5 points!

    {'color': 'green', 'points': 5}
    {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

    {'color': 'green', 'points': 5}

    - The alien is green.

    - The alien is now yellow.

    - Original x-position: 0

    - New x-position: 3

    {'color': 'green', 'points': 5}

    {'color': 'green'}

    __*__Uma lista de dicionários__*__

    {'color': 'green', 'points': 5}
    {'color': 'yellow', 'points': 10}
    {'color': 'red', 'points': 15}

    {'color': 'green', 'points': 5, 'speed': 'slow'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    ...

    Total number of aliens: 30

    {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    {'color': 'green', 'points': 5, 'speed': 'slow'}
    ...

DESCRIÇÃO
    - Um dicionário simples

    O dicionário alien_0 armazena a cor do alienígena e o valor da
    pontuação.

    - Acessando valores em um dicionário.

    Depois que o dicionário for definido, o código extrai o valor
    associado à chave 'points' do dicionário. Esse valor então é
    armazenado na variável new_points. str() converte esse valor
    inteiro em uma string e exibe uma frase sobre quantos pontos o
    jogador acabou de ganhar.

    - Adicionando novos pares chave-valor

    Começamos definindo o mesmo dicionário com o qual estávamos
    trabalhando. Em seguida, exibimos esse dicionário, mostrando uma
    imagem de suas informações.
    Acrescentamos um novo par chave-valor ao dicionário: a chave
    'x_position' e o valor 0. Fizemos o mesmo com a chave 'y_position'.
    Ao exibir o dicionário modificado, vemos os dois pares chave-valor
    adicionais.

    - Começando com um dicionário vazio.

    Definimos um dicionário alien_0 vazio e, em seguida, adicionamos
    valores para cor e pontuação. O resultado é o dicionário que usamos
    nos exemplos anteriores.

    - Modificando valores em um dicionário.

    Inicialmente, definimos um dicionário para alien_0 que contém
    apenas a cor do alienígena; em seguida, modificamos o valor
    associado à chave 'color'para 'yellow'. A saída mostra que o
    alienígena realmente mudou de verde para amarelo.

    Uma cadeia if-elif-else determina a distância que o alienígena deve
    se mover para a direita e esse valor é armazenado na variável
    x_increment. Se a velocidade do alienígena for 'slow' , ele se
    deslocará de uma unidade para a direita; se a velocidade for
    'medium' , se deslocará de duas unidades para a direita e, se for
    'fast' , se deslocará de três unidades à direita. Depois de
    calculado, o incremento é somado ao valor de x_position, e o
    resultado é armazenado no x_position dodicionário.

    - Removendo pares chave-valor

    A linha em del alien_0['points'] diz a Python para apagar a chave
    'points' do dicionário alien_0 e remover o valor associado a essa
    chave também. A saída mostra que a chave 'points' e seu valor igual
    a 5 foram apagados, porém o restante do dicionário não foi afetado.
    Saiba que o par chave-valor apagado é removido de forma permanente.

    - Uma lista de dicionários

    Inicialmente criamos três dicionários, cada um representando um
    alienígena diferente. Reunimos esses dicionários em uma lista
    chamada aliens. Por fim, percorremos a lista com um laço e exibimos
    cada alienígena.

------------------------------------------------------------------------

HISTÓRICO
    20202310: João Paulo, outubro de 2020.
        - Um dicionário simples - Pag. 131;
        - Trabalhando com dicionários - Pag. 132;
        - Acessando valores em um dicionário - Pag. 132;
        - Adicionando novos pares chave-valor - Pag. 133;
        - Começando com um dicionário vazio - Pag. 134;
        - Modificando valores em um dicionário - Pag. 134-135;
        - Removendo pares chave-valor - Pag. 136;

    20202610: João Paulo, outubro 2020.
        - Uma lista de dicionários (pg 144).

"""


alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print("\n- You just earned " + str(new_points) + " points!\n")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print("\n" + str(alien_0))

alien_0 = {'color' : 'green'}

print("\n- The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("\n- The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
alien_0['speed'] = 'fast'

print("\n- Original x-position: " + str(alien_0['x_position']))

# Move o alienígena para a direita; 
# Determina a distância que o alienígena deve se deslocar de acordo com
# sua velocidade atual.
if alien_0['speed'] == 'slow': x_increment = 1
elif alien_0['speed'] == 'medium': x_increment = 2
else: x_increment = 3 # Este deve ser um alienígena rápido

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\n- New x-position: " + str(alien_0['x_position']))

alien_0 = {'color' : 'green', 'points' : 5}
print("\n" + str(alien_0))

del alien_0['points']
print("\n" + str(alien_0)) 

print("\n__*__Uma lista de dicionários__*__\n")

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Cria uma lista vazia para armazenar alienígenas.
aliens = []

# Cria 30 alienígenas verdes.
for alien_number in range(0,30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed': 'slow'}
    aliens.append(new_alien)

print()
# Mostra os 5 primeiros alienígenas.
for alien in aliens[:5]:
    print(alien)
print("...\n")

# Mostra quantos alienígenas foram criados.
print("Total number of aliens: " + str(len(aliens)))

print()
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("...\n")
