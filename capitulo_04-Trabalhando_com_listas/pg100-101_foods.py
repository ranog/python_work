#! /usr/bin/env python3

"""
NOME
    pg100-101_foods.py

SINOPSES
    chmod +x pg100-101_foods.py
    ./pg100-101_foods.py

DESCRIÇÃO
    Exemplo das paginas 100-101, realiza a copia de uma lista de alimentos.

----------------------------------------------------------------------

HISTÓRICO
    20201510: João Paulo, outubro de 2020.
        - o código realiza e exibe a copia de uma lista de alimentos.

"""


print("- Copiando uma lista:")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n- Isso não funciona (my_foods = friend_foods:")

my_foods = friend_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
