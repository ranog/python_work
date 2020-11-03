#! /usr/bin/env python3

"""
NOME
    camiseta.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x camiseta.py
    ./camiseta.py

    Tamanho: GG
    Frase: Seja livre use Linux.

    Tamanho: M
    Frase: Piratear é ilegal. Usar Linux é legal!.

    Size: G
    Text: Eu amo Python.

    Size: G
    Text: DEFAULT.

    Size: M
    Text: DEFAULT.

    Tamanho: P
    Frase: Falar é fácil, me mostre o código.

DESCRIÇÃO
    8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite
    um tamanho e o texto de uma mensagem que deverá ser estampada na
    camiseta. A função deve exibir uma frase que mostre o tamanho da
    camiseta e a mensagem estampada.
    Chame a função uma vez usando argumentos posicionais para criar uma
    camiseta. Chame a função uma segunda vez usando argumentos nomeados.

    8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que
    as camisetas sejam grandes por default, com uma mensagem Eu amo
    Python. Crie uma camiseta grande e outra média com a mensagem
    default, e uma camiseta de qualquer tamanho com uma mensagem
    diferente.

HISTÓRICO
    20200311: João Paulo, novembro de 2020.
        - 8.3 – Camiseta (pg 177).
        - 8.4 - Camisetas grandes (pg 177).

"""


def make_shirt(tamanho, texto):
    print("Tamanho: " + tamanho.upper() + "\nFrase: " + texto + ".\n")

make_shirt('gg', 'Seja livre use Linux')
make_shirt(texto = 'Piratear é ilegal. Usar Linux é legal!', tamanho = 'm')

def make_shirts(text, size = 'g'):
    print("Size: " + size.upper() + "\nText: " + text + ".\n")

make_shirts('Eu amo Python')

def shirts(size, text = 'default'):
    print("Size: " + size.upper() + "\nText: " + text.upper() + ".\n")

shirts('g')
shirts('m')
make_shirt(tamanho = 'p', texto = 'Falar é fácil, me mostre o código')
