#! /usr/bin/env python3

"""
NOME
    print_models.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x print_models.py
    ./print_models.py
    Printing model: dodecahedron
    Printing model: robot pendant
    Printing model: iphone case

    The following models have been printed:
    dodecahedron
    robot pendant
    iphone case

DESCRIÇÃO
    8.15 – Impressão de modelos: Coloque as funções do exemplo
    print_models.py em um arquivo separado de nome
    printing_functions.py. Escreva uma instrução import no início de
    print_models.py e modifique o arquivo para usar as funções
    importadas.

HISTÓRICO1
    20200911: João Paulo, novembro de 2020.
        - 8.15 – Impressão de modelos (pg 195).

"""


from printing_functions import print_models as pm 
from printing_functions import show_completed_models as scm

# Começa com alguns designs que devem ser impressos 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)
