
#! /usr/bin/env python3

"""
NOME
    printing_functions.py - FAÇA VOCÊ MESMO.

SINOPSES
    - Importando um módulo completo:
        import printing_functions

    - Importando funções específicas:
        from printing_functions import print_models , show_completed_models
    
    - Usando a palavra reservada as para atribuir um aliasa uma função:
        from printing_functions import print_models as pm
        from printing_functions import show_completed_models as scm

    - Usando a palavra reservada as para atribuir um alias a um módulo:
        import printing_functions as pf

DESCRIÇÃO
    8.15 – Impressão de modelos: Coloque as funções do exemplo
    print_models.py em um arquivo separado de nome
    printing_functions.py. Escreva uma instrução import no início de
    print_models.py e modifique o arquivo para usar as funções
    importadas.

HISTÓRICO
    20200911: João Paulo, novembro de 2020.
        - 8.15 – Impressão de modelos (pg 195).

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
