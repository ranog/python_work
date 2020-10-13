#! /usr/bin/env python3

"""
NOME
    pg95_numbers.py

SINOPSES
    chmod +x pg95_numbers.py
    ./pg95_numbers.py

DESCRIÇÃO
    Crindo listas numéricas usando a função range() para exibir uma sequência
    de números.
----------------------------------------------------------------------

HISTÓRICO
    20201310: João Paulo, outubro de 2020.
        - implementação da função range()

"""


print("- Usando a função range():")
for value in range(1, 5):
    print(value)

print("\n- Para exibir os números de 1 a 5, você deve usar range(1, 6) :")
for value in range(1, 6):
    print(value)

print("\n- Para exibir os números de 1 a 5, você deve usar range(1,6) :")
numbers = list(range(1, 6))
print(numbers)

print("\n- Listar os números pares entre 1 e 10 (even_numbers.py):")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n- Os dez primeiros quadrados perfeitos em uma lista (squares.py):")
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print("\n- Concatenar cada novo valor diretamente na lista:")
squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print("\n- Estatísticas simples com uma lista de números:")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Lista: " + str(digits))
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n- List comprehensions (squares.py):")
squares = [value ** 2 for value in range(1, 11)]

print(squares)


