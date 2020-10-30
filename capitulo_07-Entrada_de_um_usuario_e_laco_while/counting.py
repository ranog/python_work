#! /usr/bin/env python3

"""
NOME
    counting.py - Laço while em ação.

SINOPSES
    chmod +x counting.py
    ./counting.py

    - Laço while em ação:
    1
    2
    3
    4
    5

    - Usando continue em umwhile:
    1
    3
    5
    7
    9

DESCRIÇÃO

    - Laço while em ação:

    Na primeira linha começamos a contar de 1 ao definir o valor de
    current_number com 1. O laço while é então configurado para
    continuar executando enquanto o valor de current_number for menor ou
    igual a 5. O código no laço exibe o valor current_number e então
    soma 1 a esse valor com current_number += 1 . (O operador += é um
    atalho para current_number = current_number + 1 .) Python repete o
    laço enquanto a condição current_number <= 5 for verdadeira. Como 1
    é menor que 5, Python exibe 1 e então soma 1, fazendo o número atual
    ser igual a 2 . Como 2 é menor que 5, Python exibe 2 e soma 1
    novamente, fazendo o número atual ser igual a 3 , e assim
    sucessivamente. Quando o valor de current_number for maior que 5, o
    laço para de executar e o programa termina.

    - Usando continue em um laço:

    Inicialmente, definimos current_number com 0.
    Como esse valor é menor que 10, Python entra no laço while. Uma vez
    no laço, incrementamos o contador de 1, portanto current_number
    passa a ser 1. A instrução if então verifica o módulo entre
    current_number e 2.
    Se o módulo for 0 (o que significa que current_number é divisível
    por 2), a instrução continue diz a Python para ignorar o restante do
    laço e voltar ao início. Se o número atual não for divisível por 2,
    o restante do laço será executado e Python exibirá o número atual.

    - Evitando loops infinitos:

    Agora o valor de x começará em 1, mas jamais será modificado. Como
    resultado, o teste condicional x <= 5 será sempre avaliado como True
    e o laço while executará indefinidamente, exibindo uma série de 1s.

HISTÓRICO
    20202910: João Paulo, outubro de 2020.
        - Laço while em ação (pg 157).

        - Usando continue em um laço (pg 161-162).

        - Evitando loops infinitos (pg 162-163).

"""

print("\n- Laço while em ação: ")
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n- Usando continue em um laço: ")

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

print("\n- Evitando loops infinitos: ") 
x = 1

while x <= 5:
    print(x)
    # x += 1 # esse laço executa indefinidamente!
