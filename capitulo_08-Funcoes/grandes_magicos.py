#! /usr/bin/env python3

"""
NOME
    grandes_magicos.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x grandes_magicos.py
    ./grandes_magicos.py
    O Grande David Copperfield
    O Grande Siegfried Fischbacher
    O Grande David Blaine
    O Grande Dai Vernon
    O Grande Jasper Maskelyne
    O Grande Richiardi Jr
    O Grande Fu-Manchu
    O Grande Harry Houdini

DESCRIÇÃO
    8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
    Exercício 8.9. Escreva uma função chamada make_great() que modifique
    a lista de mágicos acrescentando a expressão o Grande ao nome de
    cada mágico. Chame show_magicians() para ver se a lista foi
    realmente modificada.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - 8.10 - Grandes mágicos (pg 187).

"""


def make_great(magicians, great_magician):
    while magicians:
        temp = "o grande " + str(magicians.pop())
        great_magician.append(temp)


def show_magicians(great_magician):
    for magic in great_magician:
        print(magic.title())

magicians = ['harry houdini', 'fu-manchu', 'richiardi jr',
             'jasper maskelyne', 'dai vernon', 'david blaine',
             'siegfried fischbacher', 'david copperfield', ]
great_magician = []

make_great(magicians, great_magician)
show_magicians(great_magician)
