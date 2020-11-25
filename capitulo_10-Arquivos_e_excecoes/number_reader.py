#! /usr/bin/env python3

"""
NOME
    number_reader.py - Usando json.dump() e json.load().

SINOPSES
    chmod +x number_reader.py
    ./number_reader.py
    [2, 3, 5, 7, 11, 13]

------------------------------------------------------------------------

DESCRIÇÃO
    - Usando json.dump() e json.load():

        Em filename garantimos que o mesmo arquivo em que escrevemos os
        dados será lido. Dessa vez, quando abrirmos o arquivo, fazemos
        isso em modo de leitura, pois Python precisará apenas ler dados
        do arquivo. Usamos a função json.load() para carregfileU
        informações armazefileU em numbers.json e as guardamos na
        variável numbers. Por fim, exibimos a lista de números
        recuperada; podemos ver que é a mesma lista criada em
        number_writer.py:
        [2, 3, 5, 7, 11, 13]

        Essa é uma maneira simples de compartilhar dados entre dois
        programas.

------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Usando json.dump() e json.load() (pg 249-250).

"""


import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
