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

------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - Testando uma função (pg 257).

"""


def get_formatted_name(first, last):
    """Gera um nome completo formatado de modo elegante."""

    full_name = first + ' ' + last

    return full_name.title()
