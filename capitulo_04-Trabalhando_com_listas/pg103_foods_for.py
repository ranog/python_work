#! /usr/bin/env python3

"""
NOME
    pg103_foods_for.py

SINOPSES
    chmod +x pg103_foods_for.py
    ./pg103_foods_for.py

DESCRIÇÃO
    4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

----------------------------------------------------------------------

HISTÓRICO
    20201610: João Paulo, outubro de 2020.
        - Implementação do exercicio 4.12 – Mexercicio.

"""


print("- Copiando uma lista:")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are(laço for):")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are(laço for):")
for friend_food in friend_foods:
    print(friend_food)

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
