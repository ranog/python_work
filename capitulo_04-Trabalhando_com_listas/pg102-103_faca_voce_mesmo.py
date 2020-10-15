#! /usr/bin/env python3

"""
NOME
    pg102-103_faca_voce_mesmo.py

SINOPSES
    chmod +x pg102-103_faca_voce_mesmo.py
    ./pg102-103_faca_voce_mesmo.py

DESCRIÇÃO
    4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
    acrescente várias linhas no final do programa que façam o seguinte: • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
    • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
    • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
    exibir os três últimos itens da lista.

    4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
    (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
    Então faça o seguinte: • Adicione uma nova pizza à lista original.
    • Adicione uma pizza diferente à lista friend_pizzas.
    • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
    favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
    Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
    um laço for para exibir a segunda lista. Certifique-se de que cada pizza
    nova esteja armazenada na lista apropriada.
    
    4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
    laços for para fazer exibições a fim de economizar espaço. Escolha uma
versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

----------------------------------------------------------------------

HISTÓRICO
    20201510: João Paulo, outubro de 2020.
        - o código exite algumas fatias de uma lista.

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

print("\n\n- 4.10 – Fatias:")
my_foods.append('burger')
my_foods[3] = 'potatos'

print("\n- Lista: " + str(my_foods))
print("\nOs três primeiros itens da lista são:")
print(my_foods[0:3])

print("\nTrês itens do meio da lista são:")
print(my_foods[2:5])

print("\nOs três últimos itens da lista são:")
print(my_foods[-3:])
