#! /usr/bin/env python3

"""
NOME
    pets.py - Argumentos posicionais.

SINOPSES
    chmod +x pets.py
    ./pets.py

DESCRIÇÃO
    A definição mostra que essa função precisa de um tipo de animal e de
    seu nome. Quando chamamos describe_pet(), devemos fornecer o tipo do
    animal e um nome, nessa ordem. Por exemplo, na chamada da função, o
    argumento 'hamster' é armazenado no parâmetro animal_type e o
    argumento 'harry' é armazenado no parâmetro pet_name. No corpo da
    função, esses dois parâmetros são usados para exibir informações
    sobre o animal de estimação descrito.

HISTÓRICO
    20200211: João Paulo, outubro de 2020.
        - Argumentos posicionais (pg 172).

"""


"""Exibe informações sobre um animal de estimação."""
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
