#! /usr/bin/env python3

"""
NOME
    pg103_dimensions.py

SINOPSES
    chmod +x pg103_dimensions.py
    ./pg103_dimensions.py

DESCRIÇÃO
    No exemplo, se tivermos um retângulo que sempre deva ter determinado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões em uma tupla.

----------------------------------------------------------------------

HISTÓRICO
    20201610: João Paulo, outubro de 2020.
        - Implementacão do exemplo dimensions.py da pagina 103.

"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""
dimensions[0] = 250

Erro quando tentamos atribuir um novo valor a um item da tupla:

Traceback (most recent call last):
  File "/data/data/com.termux/files/home/python_work/capitulo_04-Trabalhando_com_listas/./pg103_dimensions.py", line 26, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
"""

print("\n- Percorrendo todos os valores de uma tupla com um laço:")

for dimension in dimensions:
    print(dimension)

print("\nSobrescrevendo uma tupla:")
print("- Original dimensions:")
for dimension in dimensions: 
    print(dimension)

dimensions = (400, 100) 
print("\n- Modified dimensions:")
for dimension in dimensions: 
    print(dimension)
