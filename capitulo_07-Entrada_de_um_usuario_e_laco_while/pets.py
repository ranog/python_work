#! /usr/bin/env python3

"""
NOME
    pets.py - Removendo todas as instâncias de valores específicos de
    uma lista.

SINOPSES
    chmod +x pets.py
    ./pets.py

DESCRIÇÃO
    Começamos com uma lista contendo várias instâncias de 'cat' . Após
    exibir a lista, Python entra no laço while , pois encontra o valor
    'cat' na lista pelo menos uma vez. Depois que entrar no laço, Python
    remove a primeira instância de 'cat', retorna à linha while e então
    entra novamente no laço quando descobre que 'cat' ainda está na
    lista. Cada instância de 'cat' é removida até que esse valor não
    esteja mais na lista; nesse momento, Python sai do laço e exibe a
    lista novamente.

HISTÓRICO
    20200111: João Paulo, outubro de 2020.
        - Removendo todas as instâncias de valores específicos de uma
        lista (pg 165).

"""


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(str(pets) + "\n")

while 'cat' in pets:
    pets.remove('cat')
    print(pets)
