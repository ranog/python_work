#! /usr/bin/env python3

"""
NOME
    favorite_numbers.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x favorite_numbers.py
    ./favorite_numbers.py

    John's favorite numbers is 7;
    Martin's favorite numbers is 11;
    Frank's favorite numbers is 3;
    Jason's favorite numbers is 13;
    James' favorite numbers is 2.

DESCRIÇÃO
    - 6.2 – Números favoritos:

    Use um dicionário para armazenar os números favoritos de algumas pessoas.
    Pense em cinco nomes e use-os como chaves em seu dicionário. Pense em um
    número favorito para cada pessoa e armazene cada um como um valor em seu
    dicionário. Exiba o nome de cada pessoa e seu número favorito. Para que
    seja mais divertido ainda, faça uma enquete com alguns amigos e obtenha
    alguns dados reais para o seu programa.

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.2 - Números favoritos - Pag. 138.

"""


favorite_numbers = {'john' : 7,
                    'martin' : 11,
                    'frank' : 3,
                    'jason' : 13,
                    'james' : 2,}

print("\nJohn's favorite numbers is " + str(favorite_numbers['john']) + ";\n" +
      "Martin's favorite numbers is " + str(favorite_numbers['martin']) + ";\n" +
      "Frank's favorite numbers is " + str(favorite_numbers['frank']) + ";\n" +
      "Jason's favorite numbers is " + str(favorite_numbers['jason']) + ";\n" +
      "James' favorite numbers is " + str(favorite_numbers['james']) + ".")
