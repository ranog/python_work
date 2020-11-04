#! /usr/bin/env python3

"""
NOME
    formatted_name.py - Devolvendo um valor simples.

SINOPSES
    chmod +x formatted_name.py
    ./formatted_name.py

    Devolvendo um valor simples:
    Jimi Hendrix

DESCRIÇÃO
    A definição de get_formatted_name() aceita um primeiro nome e um
    sobrenome como parâmetros. A função combina esses dois nomes,
    acrescenta um espaço entre eles e armazena o resultado em full_name.
    O valor de full_name é convertido para que tenha letras iniciais
    maiúsculas e é devolvido para a linha que fez a chamada.
    Quando chamamos uma função que devolve um valor, precisamos fornecer
    uma variável em que o valor de retorno possa ser armazenado.
    Nesse caso, o valor devolvido é armazenado na variável musician.

HISTÓRICO
    20200411: João Paulo, novembro de 2020.
        - Devolvendo um valor simples. (pg 178).

"""


print("\nDevolvendo um valor simples: ")

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)
