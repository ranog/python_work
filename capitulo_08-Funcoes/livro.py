#! /usr/bin/env python3

"""
NOME
    livros.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x livros.py
    ./livros.py

    Um dos meus livros favoritos é Alice no país das maravilhas.

DESCRIÇÃO
    8.2 – Livro favorito: Escreva uma função chamada favorite_book() que
    aceite um parâmetro title. A função deve exibir uma mensagem como Um
    dos meus livros favoritos é Alice no país das maravilhas. Chame a
    função e não se esqueça de incluir o título do livro como argumento
    na chamada da função.

HISTÓRICO
    20200211: João Paulo, outubro de 2020.
        - 8.2 - Livro favorito (pg 171).

"""


def favorite_book(title):
    print("\nUm dos meus livros favoritos é " + title + ".")

favorite_book('Alice no país das maravilhas')
