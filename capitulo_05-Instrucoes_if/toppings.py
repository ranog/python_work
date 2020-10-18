#! /usr/bin/env python3

"""
NOME
    toppings.py - Verificando a diferença

SINOPSES
    chmod +x toppings.py
    ./toppings.py
    Hold the anchovies!
    True
    False

DESCRIÇÃO
    Compara o valor de requested_topping com o valor 'anchovies'. Se esses
    dois valores não forem iguais, Python devolverá True e executará o código
    após a instrução if. Se esses dois valores forem iguais, Python devolverá
    False e não executará o código após essa instrução.

    A palavra reservada in diz a Python para verificar a existência de
    'mushrooms' e de 'pepperoni' na lista requested_toppings.

----------------------------------------------------------------------

HISTÓRICO
    20201710: João Paulo, outubro de 2020.
        - Implementação da função para determinar se dois valores não são
        iguais;
        - Verificando se um valor está em uma lista.

"""


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
