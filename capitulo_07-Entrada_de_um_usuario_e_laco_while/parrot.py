#! /usr/bin/env python3

"""
NOME
    parrot.py - Como afunção input() trabalha.

SINOPSES
    chmod +x parrot.py
    ./parrot.py

    Tell me something, and I will repeat it back to you:Hello everyone!
    Hello everyone!

DESCRIÇÃO
    O programa espera enquanto o usuário fornece sua resposta e continua
    depois que ele tecla ENTER. A resposta é armazenada na variável.

----------------------------------------------------------------------

HISTÓRICO
    20202810: João Paulo, outubro de 2020.
        - Como afunção input() trabalha (pg 152-153).

"""

message = input("Tell me something, and I will repeat it back to you:")

print(message)
