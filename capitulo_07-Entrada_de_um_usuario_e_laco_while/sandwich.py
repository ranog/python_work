#! /usr/bin/env python3

"""
NOME
    sandwich.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x sandwich.py
    ./sandwich.py

    7.8 - Lanchonete:
    Preparei seu sanduíche de Pastrami
    Preparei seu sanduíche de Katsu-Sando
    Preparei seu sanduíche de Bánh Mì
    Preparei seu sanduíche de Pastrami
    Preparei seu sanduíche de Roti John
    Preparei seu sanduíche de Bauru
    Preparei seu sanduíche de Vada Pav
    Preparei seu sanduíche de Pastrami
    Preparei seu sanduíche de Bauru

    Sanduíches terminados:
    Pastrami
    Katsu-Sando
    Bánh Mì
    Pastrami
    Roti John
    Bauru
    Vada Pav
    Pastrami
    Bauru

    7.9 - Sem pastrami:
    ['bauru', 'pastrami', 'vada pav', 'bauru', 'roti john', 'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']
    ['bauru', 'vada pav', 'bauru', 'roti john', 'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']
    ['bauru', 'vada pav', 'bauru', 'roti john', 'bánh mì', 'katsu-sando', 'pastrami']
    ['bauru', 'vada pav', 'bauru', 'roti john', 'bánh mì', 'katsu-sando']

    - Hoje estamos sem Pastrami. Obrigado pela compreensão.

    Estamos preparando o seu sanduíche de Katsu-Sando
    Estamos preparando o seu sanduíche de Bánh Mì
    Estamos preparando o seu sanduíche de Roti John
    Estamos preparando o seu sanduíche de Bauru
    Estamos preparando o seu sanduíche de Vada Pav
    Estamos preparando o seu sanduíche de Bauru

    Sanduíches prontos:
    katsu-sando
    bánh mì
    roti john
    bauru
    vada pav
    bauru

DESCRIÇÃO
    FAÇA VOCÊ MESMO

    7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a
    preencha com os nomes de vários sanduíches. Em seguida, crie uma
    lista vazia chamada finished_sandwiches. Percorra a lista de pedidos
    de sanduíches com um laço e mostre uma mensagem para cada pedido,
    por exemplo, Preparei seu sanduíche de atum. À medida que cada
    sanduíche for preparado, transfira-o para a lista de sanduíches
    prontos. Depois que todos os sanduíches estiverem prontos, mostre
    uma mensagem que liste cada sanduíche preparado.

    7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8,
    garanta que o sanduíche de 'pastrami' apareça na lista pelo menos
    três vezes.
    Acrescente um código próximo ao início de seu programa para exibir
    uma mensagem informando que a lanchonete está sem pastrami e, então,
    use um laço while para remover todas as ocorrências de 'pastrami' de
    sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
    finished_sandwiches.

HISTÓRICO
    20200111: João Paulo, outubro de 2020.
        - 7.8 - Lanchonete (pg 166).
        - 7.9 - Sem pastrami (pg 166-167).
"""

print("\n7.8 - Lanchonete: ")

sandwich_orders = ['bauru', 'pastrami', 'vada pav', 'bauru', 'roti john',
                   'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Preparei seu sanduíche de " + sandwich.title())
    finished_sandwiches.append(sandwich)

print("\nSanduíches terminados: ")

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

print("\n7.9 - Sem pastrami: ")

orders = ['bauru', 'pastrami', 'vada pav', 'bauru', 'roti john',
                   'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']
finished = []

print(orders)

while 'pastrami' in orders:
    orders.remove('pastrami')
    print(orders)

print("\n- Hoje estamos sem Pastrami. Obrigado pela compreensão.\n")

while orders:
    sandwiches = orders.pop()
    print("Estamos preparando o seu sanduíche de " + sandwiches.title())
    finished.append(sandwiches)

print("\nSanduíches prontos: ")
for finish in finished:
    print(finish)
