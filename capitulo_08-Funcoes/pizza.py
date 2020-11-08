#! /usr/bin/env python3

"""
NOME
    pizza.py - Passando um número arbitrário de argumentos.

SINOPSES
    nome_do_módulo.nome_da_função()

DESCRIÇÃO
    Um módulo é um arquivo terminado em .py que contém o código que
    queremos importar para o nosso programa. Vamos criar um módulo que
    contenha a função make_pizza().
    Para criar esse módulo, removeremos tudo que está no arquivo
    pizza.py, exceto a função make_pizza().

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - Passando um número arbitrário de argumentos. (pg 187-188).
        - Misturando argumentos posicionais e arbitrários (pg 188).
    
    20200811: João Paulo, novembro de 2020.
        - Importando ummódulo completo (pg 191-192).

"""


def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")

    for topping in toppings:
        print("- " + topping)
