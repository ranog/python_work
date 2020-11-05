#! /usr/bin/env python3

"""
NOME
    nomes_cidade.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x nomes_cidades.py
    ./nomes_cidades.py
    "São Paulo, Brasil"
    "Toronto, Canada"
    "Texas, Estados Unidos"

DESCRIÇÃO
    8.6 – Nomes de cidade: Escreva uma função chamada city_country()
    que aceite o nome de uma cidade e seu país. A função deve devolver
    uma string formatada assim:

    "Santiago, Chile"

    Chame sua função com pelo menos três pares cidade-país e apresente
    o valor devolvido.

HISTÓRICO
    20200411: João Paulo, outubro de 2020.
        - 8.6 – Nomes de cidade (pg 182).

"""


def city_country(cidade, pais):
    full_name = '"' + cidade + ', ' + pais + '"'

    return full_name.title()

print(city_country('são paulo', 'brasil'))
print(city_country('toronto', 'canada'))
print(city_country('texas', 'estados unidos'))
