#! /usr/bin/env python3

"""
NOME
    convidado.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x convidado.py
    ./convidado.py

------------------------------------------------------------------------

DESCRIÇÃO
    10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário. Quando ele responder, escreva o nome em um arquivo chamado guest.txt.

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - 10.3 - Convidado (pg 239).

"""


username = input("\nQual o seu nome? ")
filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(username.lower() + "\n")
