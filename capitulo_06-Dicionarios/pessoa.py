#! /usr/bin/env python3

"""
NOME
    pessoa.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x pessoa.py
    ./pessoa.py

DESCRIÇÃO
    - 6.1 – Pessoa:

    Use um dicionário para armazenar informações sobre uma pessoa que você
    conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que
    ela vive. Você deverá ter chaves como first_name, last_name, age e city.
    Mostre cada informação armazenada em seu dicionário.

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.1 - Pessoa - Pag. 138.

"""


pessoa = {'first_name' : 'johnny',
          'last_name' : 'ranog',
          'age' : 83,
          'city' : 'texas'}

print("\nNome: " + pessoa['first_name'].title() +
      "\nSobrenome: " + pessoa['last_name'].title() +
      "\nIdade: " + str(pessoa['age']) +
      "\nCidade: " + pessoa['city'].title())
