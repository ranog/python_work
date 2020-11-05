#! /usr/bin/env python3

"""
NOME
    greet_users.py - Passando uma lista para uma função.

SINOPSES
    chmod +x greet_users.py
    ./greet_users.py
    Hello, Hannah!
    Hello, Ty!
    Hello, Margot!

DESCRIÇÃO
    Definimos greet_users() para que espere uma lista de nomes, que é
    armazenada no parâmetro names. A função percorre a lista recebida
    com um laço e exibe uma saudação para cada usuário. Definimos uma
    lista de usuários e então passamos a lista usernames para
    greet_users() em nossa chamada de função.

HISTÓRICO
    20200511: João Paulo, outubro de 2020.
        - Passando uma lista para uma função (pg 182-183).

"""


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
