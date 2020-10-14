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
print(players[:4])
print(players[2:])
print(players[-3:])

print("\n- Here are the firt three players on my tean:")
for player in playerh:[:3]:
    print(player.title())
