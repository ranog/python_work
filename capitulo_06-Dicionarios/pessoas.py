#! /usr/bin/env python3

"""
NOME
    pessoas.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x pessoas.py
    ./pessoas.py

    {'first_name': 'johnny', 'last_name': 'ranog', 'age': 13,
     'city': 'texas'}
    {'first_name': 'porpeta', 'last_name': 'rafilsk', 'age': 24,
     'city': 'pinga'}
    {'first_name': 'george', 'last_name': 'jungle', 'age': 97,
     'city': 'jaca'}

DESCRIÇÃO
    6.7 – Pessoas: Comece com o programa que você escreveu no Exercício
    6.1 (página 147). Crie dois novos dicionários que representem
    pessoas diferentes e armazene os três dicionários em uma lista
    chamada people. Percorra sua lista de pessoas com um laço. À medida
    que percorrer a lista, apresente tudo que você sabe sobre cada
    pessoa.

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.7 - Pessoas (pg. 149).

"""


pessoa_0 = {'first_name' : 'johnny',
            'last_name' : 'ranog',
            'age' : 13,
            'city' : 'texas',}

pessoa_1 = {'first_name' : 'porpeta',
            'last_name' : 'rafilsk',
            'age' : 24,
            'city' : 'pinga',}

pessoa_2 = {'first_name' : 'george',
            'last_name' : 'jungle',
            'age' : 97,
            'city' : 'jaca',}

people = [pessoa_0, pessoa_1, pessoa_2]

for person in people:
    print(person)
