#! /usr/bin/env python3

"""
NOME
    confirmed_users.py - Transferindo itens de uma lista para outra.

SINOPSES
    chmod +x confirmed_users.py
    ./confirmed_users.py

DESCRIÇÃO
    Começamos com uma lista de usuários não confirmados (Alice, Brian e
    Candace) e uma lista vazia para armazenar usuários confirmados. O
    laço while executa enquanto a lista unconfirmed_users não estiver
    vazia. Nesse laço, a função pop() remove os usuários não
    verificados, um de cada vez, do final de unconfirmed_users. Nesse
    caso, como Candace é o último elemento da lista unconfirmed_users,
    seu nome será o primeiro a ser removido, armazenado em current_user
    e adicionado à lista confirmed_users. O próximo é Brian e, depois,
    Alice.

HISTÓRICO
    20203110: João Paulo, outubro de 2020.
        - Transferindo itens de uma lista para outra (pg 164).

"""


print("\n- Transferindo itens de uma lista para outra: ")

# Começa com os usuários que precisam ser verificados e com uma lista
# vazia para armazenar os usuários confirmados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados
print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
