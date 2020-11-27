#! /usr/bin/env python3

"""
NOME
    names.py - Testando uma função.

SINOPSES
    $ chmod +x names.py
    $ ./names.py
    Enter 'q' at any time to quit.
    Please give me a first name: janis
    Please give me a last name: joplin
	    Neatly formatted name: Janis Joplin.
    Please give me a first name: bob
    Please give me a last name: dylan
	    Neatly formatted name: Bob Dylan.
    Please give me a first name: q

------------------------------------------------------------------------

DESCRIÇÃO
    O programa names.py permite que os usuários forneçam um primeiro
    nome e um sobrenome e vejam um nome completo formatado de modo
    elegante.

    Esse programa importa get_formatted_name() de name_function.py. O
    usuário pode fornecer uma série de primeiros nomes e de sobrenomes e
    ver os nomes completos formatados.

------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - Testando uma função (pg 257).

"""


from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")

while True:

    first = input("Please give me a first name: ")
    if first.lower() == 'q':
        break

    last = input("Please give me a last name: ")
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
