#! /usr/bin/env python3

"""
NOME
    counting.py - Laço while em ação.

SINOPSES
    chmod +x counting.py
    ./counting.py
    1
    2
    3
    4
    5

DESCRIÇÃO
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

HISTÓRICO
    20202910: João Paulo, outubro de 2020.
        - Laço while em ação (pg 157).

"""


current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
