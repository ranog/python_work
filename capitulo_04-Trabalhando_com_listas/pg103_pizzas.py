#! /usr/bin/env python3

"""
NOME
    pg103_pizzas.py

SINOPSES
    chmod +x pg103_pizzas.py
    ./pg103_pizzas.py

DESCRIÇÃO
    4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1 (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte:
    • Adicione uma nova pizza à lista original.
    • Adicione uma pizza diferente à lista friend_pizzas.
    • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilizevum laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.

----------------------------------------------------------------------

HISTÓRICO
    20201610: João Paulo, outubro de 2020.
        - Implementação do exercicio 4.11 – Minhas pizzas, suas pizzas

"""

pizzas = ['Muçarela', 'Calabresa', 'Marguerita']
pizzas_amigo = pizzas[:]

pizzas.append('Napolitana')
pizzas_amigo.append('Frango com catupiry')

print('- Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)

print('\n- As pizzas favoritas de meu amigo são:')
for pizza_amigo in pizzas_amigo:
    print(pizza_amigo)
