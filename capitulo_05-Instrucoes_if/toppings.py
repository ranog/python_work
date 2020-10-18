#! /usr/bin/env python3

"""
NOME
    toppings.py - Verificando a diferença

SINOPSES
    chmod +x toppings.py
    ./toppings.py
    Hold the anchovies!

DESCRIÇÃO
    Compara o valor de requested_topping com o valor 'anchovies'. Se esses
    dois valores não forem iguais, Python devolverá True e executará o código
    após a instrução if. Se esses dois valores forem iguais, Python devolverá
    False e não executará o código após essa instrução.

----------------------------------------------------------------------

HISTÓRICO
    20201710: João Paulo, outubro de 2020.
        - Implementação da função para determinar se dois valores não são
        iguais.

"""


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
