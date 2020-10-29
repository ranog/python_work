#! /usr/bin/env python3

"""
NOME
    even_or_odd.py - Operador de módulo.

SINOPSES
    chmod +x even_or_odd.py
    ./even_or_odd.py
    Enter a number, and I'll tell you if it's even or odd: 42

    The number 42 is even.

    Enter a number, and I'll tell you if it's even or odd: 13

    The number 13 is odd.

DESCRIÇÃO
    Números pares são sempre divisíveis por dois, portanto, se o módulo
    entre um número e dois for zero (nesse caso, if number % 2 == 0), o
    número será par. Caso contrário, será ímpar.

HISTÓRICO
    20202910: João Paulo, outubro de 2020.
        - Operador de módulo (pg 155-156).

"""


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")

else:
    print("\nThe number " + str(number) + " is odd.")
