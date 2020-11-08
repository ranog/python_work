#! /usr/bin/env python3

"""
NOME
    carros.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x carros.py
    ./carros.py
    {'fabricante_carro': 'subaru', 'modelo_carro': 'outback',
    'color': 'blue', 'tow_package': True}

DESCRIÇÃO
    8.14 – Carros: Escreva uma função que armazene informações sobre um
    carro em um dicionário. A função sempre deve receber o nome de um
    fabricante e um modelo. Um número arbitrário de argumentos nomeados
    então deverá ser aceito. Chame a função com as informações
    necessárias e dois outros pares nome-valor, por exemplo, uma cor ou
    um opcional. Sua função deve ser apropriada para uma chamada como
    esta: car = make_car('subaru', 'outback', color='blue',
    tow_package=True) Mostre o dicionário devolvido para garantir que
    todas as informações foram armazenadas corretamente.

HISTÓRICO
    20200811: João Paulo, outubro de 2020.
        - 8.14 - Carros (pg 190).

"""


def make_car(fabricante, modelo, **carro_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um
    carro."""

    carro = {}

    carro['fabricante_carro'] = fabricante
    carro['modelo_carro'] = modelo

    for key, value in carro_info.items():
        carro[key] = value

    return carro

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

print(car)
