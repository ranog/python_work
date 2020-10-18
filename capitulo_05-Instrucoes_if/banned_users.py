#! /usr/bin/env python3

"""
NOME
    banned_users.py - Verificando se um valor não está em uma lista

SINOPSES
    chmod +x banned_users.py
    ./banned_users.py
    Marie, you can post a response if you wish.

DESCRIÇÃO
    Em algumas ocasiões é importante saber se um valor não está em uma lista.
    Podemos usar a palavra reservada not nesse caso.

    Se o valor de user não estiver na lista banned_users, Python devolverá
    True e executará a linha indentada.

----------------------------------------------------------------------

HISTÓRICO
    20201810: João Paulo, outubro de 2020.
        - Verificando se um valor não está em uma lista.

"""


banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
