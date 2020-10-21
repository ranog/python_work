#! /usr/bin/env python3

"""
NOME
    alien_color.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x alien_color.py
    ./alien_color.py

    - You won 10 points.

    - You won 5 points.

    - You won 5 points (green).

    - You won 10 points (yellow).

    - You won 15 points (red).

DESCRIÇÃO
    5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser
    atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe
    um valor igual a 'green', 'yellow' ou 'red'.
    
    • Escreva uma instrução if para testar se a cor do alienígena é verde. Se
    for, mostre uma mensagem informando que o jogador acabou de ganhar cinco
    pontos.

    • Escreva uma versão desse programa em que o teste if passe e outro em que
    ele falhe. (A versão que falha não terá nenhuma saída.)

    5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como
    foi feito no Exercício 5.3, e escreva uma cadeia if-else.

    • Se a cor do alienígena for verde, mostre uma frase informando que o
    jogador acabou de ganhar cinco pontos por atingir o alienígena.

    • Se a cor do alienígena não for verde, mostre uma frase informando que o
    jogador acabou de ganhar dez pontos.

    • Escreva uma versão desse programa que execute o bloco if e outro que
    execute o bloco else.

    5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício
    5.4 em uma cadeia if-elif-else.

    • Se o alienígena for verde, mostre uma mensagem informando que o jogador
    ganhou cinco pontos.

    • Se o alienígena for amarelo, mostre uma mensagem informando que o
    jogador ganhou dez pontos.
   
    • Se o alienígena for vermelho, mostre uma mensagem informando que o
    jogador ganhou quinze pontos.

    • Escreva três versões desse programa, garantindo que cada mensagem seja
    exibida para a cor apropriada do alienígena.

----------------------------------------------------------------------

HISTÓRICO
    20202110: João Paulo, outubro de 2020.
        - 5.3 – Cores de alienígenas #1 (Pag. 123);
        - 5.4 – Cores de alienígenas #2 (Pag. 123);
        - 5.5 – Cores de alienígenas #3 (Pag. 123);

"""


alien_color = 'red'
if alien_color == 'green': points = 5
else: points = 10
print("\n- You won " +  str(points) + " points.")

alien_color = 'green'
if alien_color == 'green': points = 5
else: points = 10
print("\n- You won " +  str(points) + " points.")


if alien_color == 'green': points = 5
elif alien_color == 'yellow': points = 10
else: points = 15
print("\n- You won " +  str(points) + " points (" + alien_color + ").")

alien_color = 'yellow'
if alien_color == 'green': points = 5
elif alien_color == 'yellow': points = 10
else: points = 15
print("\n- You won " +  str(points) + " points (" + alien_color + ").")

alien_color = 'red'
if alien_color == 'green': points = 5
elif alien_color == 'yellow': points = 10
else: points = 15
print("\n- You won " +  str(points) + " points (" + alien_color + ").")
