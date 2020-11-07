#! /usr/bin/env python3

"""
NOME
    magicos.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x magicos.py
    ./magicos.py
    Mágicos famosos:
    - Harry Houdini
    - Fu-Manchu
    - Richiardi Jr
    - Jasper Maskelyne
    - Dai Vernon
    - David Blaine
    - Siegfried Fischbacher
    - David Copperfield

DESCRIÇÃO
    8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista
    para uma função chamada show_magicians() que exiba o nome de cada
    mágico da lista.

HISTÓRICO
    20200611: João Paulo, outubro de 2020.
        - 8.10 - Grandes mágicos (pg 187).

"""


def show_magicians(magicians):
    for magic in magicians:
        print("- " + magic)

magicians = ['Harry Houdini', 'Fu-Manchu', 'Richiardi Jr',
             'Jasper Maskelyne', 'Dai Vernon', 'David Blaine',
             'Siegfried Fischbacher', 'David Copperfield', ]

print("\nMágicos famosos: ")
show_magicians(magicians)
