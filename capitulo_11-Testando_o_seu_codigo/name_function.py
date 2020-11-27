#! /usr/bin/env python3

"""
NOME
    name_function.py - Testando uma função.

SINOPSES
    from name_function import get_formatted_name

------------------------------------------------------------------------

DESCRIÇÃO
    A função get_formatted_name() combina o primeiro nome e o sobrenome
    com um espaço entre eles para compor um nome completo e então
    converte as primeiras letras do nome para maiúsculas e devolve o
    nome completo.

    Nessa nova versão de get_formatted_name(), o nome do meio é
    opcional. Se um nome do meio for passado para a função (if middle:),
    o nome completo conterá um primeiro nome, um nome do meio e um
    sobrenome. Caso contrário, o nome completo será constituído apenas
    de um primeiro nome e de um sobrenome.

------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - Testando uma função (pg 257).

    20202711: João Paulo, novembro de 2020.
        - Um teste que falha (pg 260-261).
        - Respondendo a um teste que falhou (pg 261-262)


"""


def get_formatted_name(first, last, middle=''):
    """Gera um nome completo formatado de modo elegante."""

    if middle:
        full_name = first + ' ' + middle + ' ' + last

    else:
        full_name = first + ' ' + last

    return full_name.title()
