#! /usr/bin/env python3

"""
NOME
    pizza.py - Passando um número arbitrário de argumentos.

SINOPSES
    chmod +x pizza.py
    ./pizza.py

    ## Parte comentada na função ##

    ('pepperoni',)
    ('mushrooms', 'green peppers', 'extra cheese')

------------------------------------------------------------------------

    ## Passando um número arbitrário de argumentos. ##

    Making a pizza with the following toppings:
    - pepperoni

    Making a pizza with the following toppings:
    - mushrooms
    - green peppers
    - extra cheese

------------------------------------------------------------------------

    ## Misturando argumentos posicionais e arbitrários. ##

    Making a 16-inch pizza with the following toppings:
    - pepperoni

    Making a 12-inch pizza with the following toppings:
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

    - Misturando argumentos posicionais e arbitrários

    O parâmetro que aceita um número arbitrário de argumentos deve ser
    colocado por último na definição da função. Python faz a
    correspondência de argumentos posicionais e nomeados antes, e depois
    agrupa qualquer argumento remanescente no último parâmetro.

    Na definição da função, Python armazena o primeiro valor recebido no
    parâmetro size. Todos os demais valores que vierem depois são
    armazenados na tupla toppings. As chamadas da função incluem um
    argumento para o tamanho antes, seguido de tantos ingredientes
    quantos forem necessários.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - Passando um número arbitrário de argumentos. (pg 187-188).
        - Misturando argumentos posicionais e arbitrários (pg 188).

"""


def make_pizza(size, *toppings):
    """Exibe a lista de ingredientes pedidos."""
    #print(toppings)

    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")

    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
