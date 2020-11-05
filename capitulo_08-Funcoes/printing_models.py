#! /usr/bin/env python3

"""
NOME
    printing_models.py - Modificando uma lista em uma função.

SINOPSES
    chmod +x printing_models.py
    ./printing_models.py

DESCRIÇÃO

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
