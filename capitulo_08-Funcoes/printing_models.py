#! /usr/bin/env python3

"""
NOME
    printing_models.py - Modificando uma lista em uma função.

SINOPSES
    chmod +x printing_models.py
    ./printing_models.py
    Printing model: dodecahedron

    The following models have been printed:
    dodecahedron
    Printing model: robot pendant

    The following models have been printed:
    dodecahedron
    robot pendant
    Printing model: iphone case

    The following models have been printed:
    dodecahedron
    robot pendant
    iphone case

DESCRIÇÃO
    Esse programa começa com uma lista de designs que devem ser
    impressos e uma lista vazia chamada completed_models para a qual
    cada design será transferido após a impressão. Enquanto houver
    designs em unprinted_designs, o laço while simulará a impressão de
    cada um deles removendo um design do final da lista, armazenando-o
    em current_design e exibindo uma mensagem informando que o design
    atual está sendo impresso. O design então é adicionado à lista de
    modelos finalizados. Quando o laço acaba de executar, uma lista de
    designs impressos é exibida.

HISTÓRICO
    20200511: João Paulo, outubro de 2020.
        - Modificando uma lista em uma função (pg 183-186).

"""


# Começa com alguns designs que devem ser impressos 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum 
# Transfere cada design para completed_models após a impressão

while unprinted_designs:
    current_design = unprinted_designs.pop()

# Simula a criação de uma impressão 3D a partir do design
    print("Printing model: " + current_design)

    completed_models.append(current_design)

    # Exibe todos os modelos finalizados 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)
