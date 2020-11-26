#! /usr/bin/env python3

"""
NOME
    numero_favorito.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x numero_favorito.py
    ./numero_favorito.py
    - Qual é o seu número favorito? 13
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

num_favorito = input("- Qual é o seu número favorito? ")
arquivo = 'numero_favorito.json'

with open(arquivo, 'w') as obj_arq:
    json.dump(num_favorito, obj_arq)
