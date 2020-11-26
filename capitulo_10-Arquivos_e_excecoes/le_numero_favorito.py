#! /usr/bin/env python3

"""
NOME
    le_numero_favorito.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x le_numero_favorito.py
    ./le_numero_favorito.py
    Eu sei qual é o seu número favorito! É 13.

------------------------------------------------------------------------

DESCRIÇÃO
    10.11 – Número favorito:
        Escreva um programa que pergunte qual é o número favorito de um
        usuário. Use json.dump() para armazenar esse número em um
        arquivo. Escreva um programa separado que leia esse valor e
        apresente a mensagem “Eu sei qual é o seu número favorito! É
        _____.”.
------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - 10.11 – Número favorito (pg 254). 

"""


import json

arquivo = 'numero_favorito.json'

with open(arquivo) as obj_arq:
    num_favorito = json.load(obj_arq)

print("Eu sei qual é o seu número favorito! É " + num_favorito)
