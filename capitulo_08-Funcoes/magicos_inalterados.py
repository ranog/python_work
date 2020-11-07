#! /usr/bin/env python3

"""
NOME
    magicos_inalterados.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x magicos_inalterados.py
    ./magicos_inalterados.py
    O Grande David Copperfield
    O Grande Siegfried Fischbacher
    O Grande David Blaine
    O Grande Dai Vernon
    O Grande Jasper Maskelyne
    O Grande Richiardi Jr
    O Grande Fu-Manchu
    O Grande Harry Houdini

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
    8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício
    8.10. Chame a função make_great() com uma cópia da lista de nomes de
    mágicos. Como a lista original não será alterada, devolva a nova
    lista e armazene-a em uma lista separada. Chame show_magicians() com
    cada lista para mostrar que você tem uma lista de nomes originais e
    uma lista com a expressão o Grande adicionada ao nome de cada
    mágico.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - 8.11 - Mágicos inalterados (pg 187).

"""


def make_great(magicians, great_magicians):
    while magicians:
        temp = "o grande " + str(magicians.pop())
        great_magicians.append(temp)

def show_magicians(great_magicians, magicians):
    for great_magician in great_magicians:
        print(great_magician.title())

    print("\nMágicos famosos: ")

    for magic in magicians:
        print("- " + magic.title())

magicians = ['harry houdini', 'fu-manchu', 'richiardi jr',
             'jasper maskelyne', 'dai vernon', 'david blaine',
             'siegfried fischbacher', 'david copperfield', ]
great_magicians = []

# enviando uma cópia da lista magicians para a função make_great
make_great(magicians[:], great_magicians)
show_magicians(great_magicians, magicians)
