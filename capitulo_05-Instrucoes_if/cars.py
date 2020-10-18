#! /usr/bin/env python3

"""
NOME
    cars.py - Um exemplo simples

SINOPSES
    chmod +x cars.py
    ./cars.py
    Audi
    BMW
    Subaru
    Toyota

DESCRIÇÃO
    O laço nesse exemplo inicialmente verifica se o valor atual de car é 'bmw'.
    Em caso afirmativo, o valor é exibido com letras maiúsculas. Se o valor de 
    car for diferente de 'bmw', será exibido com a primeira letra maiúscula.

----------------------------------------------------------------------

HISTÓRICO
    20201710: João Paulo, outubro de 2020.
        - Implementação da instrução if.

"""

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

