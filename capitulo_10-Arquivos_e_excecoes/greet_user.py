#! /usr/bin/env python3

"""
NOME
    greet_user.py - Salvando e lendo dados gerados pelo usuário.

SINOPSES
    chmod +x greet_user.py
    ./greet_user.py
    - Welcome back, Eric!

------------------------------------------------------------------------

DESCRIÇÃO
    - Salvando e lendo dados gerados pelo usuário:
        Usamos json.load() para ler as informações armazenadas em
        username.json na variável username. Agora que recuperamos o nome
        do usuário, podemos lhe desejar as boas-vindas de volta.

------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Salvando e lendo dados gerados pelo usuário (pg 250-252).

"""


import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)

print("- Welcome back, " + username.title() + "!")
