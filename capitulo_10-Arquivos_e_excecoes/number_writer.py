#! /usr/bin/env python3

"""
NOME
    number_writer.py - Usando json.dump() e json.load().

SINOPSES
    chmod +x number_writer.py
    ./number_writer.py


------------------------------------------------------------------------

DESCRIÇÃO
    - Usando json.dump() e json.load():
        Inicialmente importamos o módulo json e criamos uma lista de
        números com a qual trabalharemos. Escolhemos o nome de um
        arquivo em que armazenaremos a lista de números. É comum usar a
        extensão de arquivo .json para indicar que os dados do arquivo
        estão armazenados em formato JSON. Em seguida, abrimos o arquivo
        em modo de escrita, o que permite a json escrever os dados no
        arquivo. Usamos a função json.dump() para armazenar a lista
        numbers no arquivo numbers.json.

------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Usando json.dump() e json.load() (pg 249-250).

"""


import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
