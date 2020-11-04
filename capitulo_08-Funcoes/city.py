#! /usr/bin/env python3

"""
NOME
    city.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x city.py
    ./city.py
    Brazzaville está localizada no Congo.

    Akana está localizada no Congo.

    São Paulo está localizada no Brasil.

DESCRIÇÃO
    8.5 – Cidades: Escreva uma função chamada describe_city() que aceite
    o nome de uma cidade e seu país. A função deve exibir uma frase
    simples, como Reykjavik está localizada na Islândia. Forneça um
    valor default ao parâmetro que representa o país. Chame sua função
    para três cidades diferentes em que pelo menos uma delas não esteja
    no país default.

HISTÓRICO
    20200311: João Paulo, novembro de 2020.
        - 8.5 - Cidades (pg 177).

"""


def describe_city(city, country = 'congo'):
    print(city.title() + " está localizada no " + country.title() + ".\n")

describe_city('brazzaville')
describe_city('akana')
describe_city(city = 'são paulo', country = 'brasil')
