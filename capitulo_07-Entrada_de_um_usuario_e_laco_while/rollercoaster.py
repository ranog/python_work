#! /usr/bin/env python3

"""
NOME
    rollercoaster.py - Usando int() para aceitar entradas numéricas.

SINOPSES
    chmod +x rollercoaster.py
    ./rollercoaster.py
    How tall are yinputn inches? 71

    You're tall enough to ride!

    How tall are yinputn inches? 35

    You'll be able to ride when you're a little older.

DESCRIÇÃO
    O programa é capaz de comparar height com 36 porque height =
    int(height) converte o valor de entrada em uma representação
    numérica antes de fazer a comparação. Se o número fornecido for
    maior ou igual a 36, diremos ao usuário que sua altura é suficiente.

HISTÓRICO
    20202910: João Paulo, outubro de 2020.
        - Usando int() para aceitar entradas numéricas (pg 155).

"""


height = input("How tall are yinputn inches? ")

height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")

else:
    print("\nYou'll be able to ride when you're a little older.")
