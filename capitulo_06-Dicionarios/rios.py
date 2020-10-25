#! /usr/bin/env python3

"""
NOME
    rios.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x rios.py
    ./rios.py
    O Amazonas corre pelo Brasil.
    O Mississipi corre pelo Estados Unidos.
    O Danúbio corre pela Alemanha.

DESCRIÇÃO
    - 6.5 – Rios: 

    Crie um dicionário que contenha três rios importantes e o país que
    cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.

    • Use um laço para exibir uma frase sobre cada rio, por exemplo, O
    Nilo corre pelo Egito.

    • Use um laço para exibir o nome de cada rio incluído no dicionário.

    • Use um laço para exibir o nome de cada país incluído no
    dicionário.

------------------------------------------------------------------------

HISTÓRICO
    20202510: João Paulo, outubro de 2020
        - FAÇA VOCÊ MESMO 6.5 - Rios (pg 143).

"""


rios = {'amazonas' : 'brasil', 
        'mississipi' : 'estados unidos',
        'danúbio' : 'alemanha',}

for rio, pais in rios.items():
    if pais.lower() == 'alemanha':
        print("O " + rio.title() + " corre pela " + pais.title() + ".")
    else:
        print("O " + rio.title() + " corre pelo " + pais.title() + ".")
