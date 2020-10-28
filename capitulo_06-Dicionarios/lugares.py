#! /usr/bin/env python3

"""
NOME
    lugares .py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x lugares.py
    ./lugares.py

    John's favorite places are:
	    - Massambaba
	    - Praia Da Pontinha

    Martin's favorite place is Praia Do Forte.

    Frank's favorite places are:
	    - Praia Do Forte
	    - Forte São Matheus

    Jason's favorite place is Sitio Ilha Do Lazer.

    James's favorite places are:
	    - Massambaba
	    - Hotel Fazenda
	    - Praia Do Forte

DESCRIÇÃO
    6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places.
    Pense em três nomes para usar como chaves do dicionário e armazene
    de um a três lugares favoritos para cada pessoa. Para deixar este
    exercício um pouco mais interessante, peça a alguns amigos que
    nomeiem alguns de seus lugares favoritos. Percorra o dicionário com
    um laço e apresente o nome de cada pessoa e seus lugares favoritos.

HISTÓRICO
    20202710: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO / 6.9 - Lugares favoritos (pg 149-150).

"""


favorite_places = {
    'john' : ['massambaba', 'praia da pontinha'],
    'martin' : ['praia do forte'],
    'frank' : ['praia do forte' , 'forte são matheus'],
    'jason' : ['sitio ilha do lazer'],
    'james' : ['massambaba', 'hotel fazenda', 'praia do forte'],}

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + "'s favorite places are: ")

        for place in places:
            print("\t- " + place.title())

    else:
        print("\n" + name.title() + "'s favorite place is " +
              places[0].title()  + ".")
