#! /usr/bin/env python3

"""
NOME
    pizza.py - Passando um número arbitrário de argumentos.

SINOPSES
    chmod +x pizza.py
    ./pizza.py
    #Parte comentada na função
    ('pepperoni',) 
    ('mushrooms', 'green peppers', 'extra cheese')

    Making a pizza with the following toppings:
    - pepperoni

    Making a pizza with the following toppings:
    - mushrooms
    - green peppers
    - extra cheese

DESCRIÇÃO
    O asterisco no nome do parâmetro *toppings diz a Python para criar
    uma tupla vazia chamada toppings e reunir os valores recebidos nessa
    tupla. A instrução print no corpo da função gera uma saída que
    mostra que Python é capaz de tratar uma chamada de função com um
    valor e outra chamada com três valores. As chamadas são tratadas de
    modo semelhante. Observe que Python agrupa os argumentos em uma
    tupla, mesmo que a função receba apenas um valor.

    A função responde de forma apropriada, independentemente de receber
    um ou três valores.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - Passando um número arbitrário de argumentos. (pg 187-188).

"""


def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    #print(toppings)

    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings: ")

    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
