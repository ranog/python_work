#! /usr/bin/env python3

"""
NOME
    lembra_num_favorito.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x lembra_num_favorito.py
    ./lembre_num_favorito.py
    - Qual é o seu número favorito? 13
    Agora eu sei, é 13.

    Eu sei qual é o seu número favorito! É 13.

------------------------------------------------------------------------

DESCRIÇÃO
    10.12 – Lembrando o número favorito:
        Combine os dois programas do Exercício 10.11 em um único
        arquivo. Se o número já estiver armazenado, informe o número
        favorito ao usuário. Caso contrário, pergunte ao usuário qual é 
        o seu número favorito e armazene-o em um arquivo. Execute o
        programa duas vezes para garantir que ele funciona.

------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - 10.12 – Lembrando o número favorito (pg 254). 

"""


import json



def le_num_favorito():
    """Retorna o número favorito do usuario já armazenado."""

    try:
        arquivo = 'numero_favorito.json'

        with open(arquivo) as obj_arq:
            num_favorito = json.load(obj_arq)

    except FileNotFoundError:
        return None
    else:
        return num_favorito


def novo_numero():
    """Pede um novo número para o usuário."""
    
    num_favorito = input("- Qual é o seu número favorito? ")
    arquivo = 'numero_favorito.json'

    with open(arquivo, 'w') as obj_arq:
        json.dump(num_favorito, obj_arq)

    return num_favorito


def lembra_num_favorito():
    """Lembra o número favorito do usuário."""

    num_favorito = le_num_favorito()

    if num_favorito:
        print("Eu sei qual é o seu número favorito! É " +
            num_favorito + ".")

    else:
        num_favorito = novo_numero()
        print("Agora eu sei, é " + num_favorito + ".")


lembra_num_favorito()
