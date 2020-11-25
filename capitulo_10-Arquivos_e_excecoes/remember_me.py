#! /usr/bin/env python3

"""
NOME
    remenber_me.py - .

SINOPSES
    chmod +x remenber_me.py
    ./remenber_me.py

------------------------------------------------------------------------

DESCRIÇÃO
    Pedimos o nome do usuário para que seja armazenado. Em seguida,
    usamos json.dump(), passando-lhe um nome de usuário e um objeto
    arquivo em que esse nome será armazenado. Então exibimos uma
    mensagem informando o usuário que armazenamos suas informações.

------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Salvando e lendo dados gerados pelo usuário (pg 250-252).

"""


import json

username = input("- What is your name? ")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)

print("We'll remember you when you come back, " + username.title() + "!")
