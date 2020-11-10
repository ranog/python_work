#! /usr/bin/env python3

"""
NOME
    person_functions.py FAÇA VOCÊ MESMO.

SINOPSES
    import person_functions
    from person_functions import build_person
    from person_functions import build_person as bp
    import person_functions as pf
    from person_functions import *

DESCRIÇÃO
    8.16 – Importações: Usando um programa que você tenha escrito e que
    contenha uma única função, armazene essa função em um arquivo
    separado.
    Importe a função para o arquivo principal de seu programa e chame-a
    usando cada uma das seguintes abordagens:
    import nome_do_módulo
    from nome_do_módulo import nome_da_função
    from nome_do_módulo import nome_da_função as nf
    import nome_do_módulo as nm
    from nome_do_módulo import *

HISTÓRICO
    20201011: João Paulo, novembro de 2020.
    - 8.16 – Importações (pg 195).

"""


def build_person(first_name, last_name, age = ''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first' : first_name, 'last' : last_name}

    if age:
        person['age'] = age

    return person
