#! /usr/bin/env python3

"""
NOME
    pg99_players.py

SINOPSES
    chmod +x pg99_players.py
    ./pg99_players.py

DESCRIÇÃO
----------------------------------------------------------------------

HISTÓRICO
    20201410: João Paulo, outubro de 2020.
        - o código exibe uma fatia de uma lista de jogadores.

"""


print("- Fatiando uma lista: ")
players = ['charles', 'martina', 'michael','florence','eli']

print("\n- Lista: " + str(players))
print(players[0:3])
print(players[1:4])
