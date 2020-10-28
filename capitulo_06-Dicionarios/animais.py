#! /usr/bin/env python3

"""
NOME
    animais.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x animais.py
    ./animais.py
    {'cão': 'joao'}
    {'gato': 'denise'}
    {'porco': 'nogueira'}


DESCRIÇÃO
    6.8 – Animais de estimação: Crie vários dicionários, em que o nome
    de cada dicionário seja o nome de um animal de estimação. Em cada
    dicionário, inclua o tipo do animal e o nome do dono. Armazene esses
    dicionários em uma lista chamada pets. Em seguida, percorra sua
    lista com um laço e, à medida que fizer isso, apresente tudo que
    você sabe sobre cada animal de estimação.

----------------------------------------------------------------------

HISTÓRICO
    20202710: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO / 6.8 - Animais de estimação (pg. 149).

"""


merlot = {'cão' : 'joao'}
ravioli = {'gato' : 'denise'}
esterco = {'porco' : 'nogueira'}

pets = [merlot, ravioli, esterco]

for pet in pets:
    print(pet)
