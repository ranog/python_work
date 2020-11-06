#! /usr/bin/env python3

"""
NOME
    printing_models_1.py - Modificando uma lista em uma função.

SINOPSES
    chmod +x printing_models_1.py
    ./printing_models_1.py
    Printing model: dodecahedron
    Printing model: robot pendant
    Printing model: iphone case

    The following models have been printed:
    dodecahedron
    robot pendant
    iphone case

DESCRIÇÃO
    Definimos a função print_models() com dois parâmetros: uma lista de
    designs a serem impressos e uma lista de modelos concluídos. Dadas
    essas duas listas, a função simula a impressão de cada design
    esvaziando a lista de designs não impressos e preenchendo a lista de
    designs completos. Definimos a função show_completed_models() com um
    parâmetro: a lista de modelos finalizados. Dada essa lista,
    show_completed_models() exibe o nome de cada modelo impresso.

    Definimos uma lista de designs não impressos e uma lista vazia que
    armazenará os modelos finalizados. Então, como já definimos nossas
    duas funções, tudo que temos a fazer é chamá-las e passar os
    argumentos corretos a elas. Chamamos print_models() e passamos as
    duas listas de que essa função precisa; conforme esperado,
    print_models() simula a impressão dos designs. Em seguida, chamamos
    show_completed_models() e passamos uma lista dos modelos concluídos
    para que ela possa apresentar os modelos impressos. Os nomes
    descritivos das funções permitem que outras pessoas leiam esse
    código e o entendam, mesmo que não haja comentários.

    A primeira função imprime cada design, enquanto a segunda mostra os
    modelos concluídos.

HISTÓRICO
    20200611: João Paulo, outubro de 2020.
        - Modificando uma lista em uma função (pg 183-186).

"""


def print_models(unprinted_designs, completed_models):

    """ Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)

        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)


# Começa com alguns designs que devem ser impressos 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
