#! /usr/bin/env python3

"""
NOME
    word_count.py - Trabalhando com vários arquivos.

SINOPSES
    chmod +x word_count.py
    ./word_count.py

------------------------------------------------------------------------

DESCRIÇÃO
        A maior parte desse código não foi alterada. Simplesmente,
        indentamos o código e o movemos para o corpo de count_words().
        Manter os comentários atualizados é um bom hábito quando
        modificamos um programa; assim, transformamos o comentário em
        uma docstring e o alteramos um pouco.

------------------------------------------------------------------------

HISTÓRICO
    20202311: João Paulo, novembro de 2020.
        - Trabalhando com vários arquivos (pg 245-246).

"""


def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo.
    """

    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " deos not exist."
    
        print(msg)

    else:
        # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)

        print("\nThe file " + filename + " has about " + str(num_words) + " words.")
