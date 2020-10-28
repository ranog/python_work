#! /usr/bin/env python3

"""
NOME
    numeros_favoritos.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x numeros_favoritos.py
    ./numeros_favoritos.py

DESCRIÇÃO
    6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2
    (página 147) para que cada pessoa possa ter mais de um número
    favorito. Em seguida, apresente o nome de cada pessoa, juntamente
    com seus números favoritos.

----------------------------------------------------------------------

HISTÓRICO
    20202710: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO / 6.10 - Números favoritos - Pag. 150.

"""


favorite_numbers = {'john' : [7, 13],
                    'martin' : [11, 23, 29],
                    'frank' : [3, 2, 1, 41],
                    'jason' : [13],
                    'james' : [2, 5],}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(name.title() + "'s favorite number is " + str(numbers) + ".")

    else:
        print(name.title() + "'s favorite numbers is " + str(numbers) + ".")
