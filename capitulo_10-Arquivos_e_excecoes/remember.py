#! /usr/bin/env python3

"""
NOME
    remenber.py - Salvando e lendo dados gerados pelo usuário.

SINOPSES
    chmod +x remember.py
    ./remember.py

------------------------------------------------------------------------

DESCRIÇÃO
    - Salvando e lendo dados gerados pelo usuário:
        Não há nenhum código novo aqui; os blocos de código dos dois
        últimos exemplos simplesmente foram combinados em um só arquivo.
        Tentamos abrir o arquivo username.json. Se esse arquivo existir,
        lemos o nome do usuário de volta para a memória e exibimos uma
        mensagem desejando boas-vindas de volta ao usuário no bloco
        else. Se essa é a primeira vez que o usuário executa o programa,
        username.json não existirá e um FileNotFoundError ocorrerá.
        Python prosseguirá para o bloco except, em que pedimos ao
        usuário que forneça o seu nome. Então usamos json.dump() para
        armazenar o nome do usuário e exibimos uma saudação.

        Qualquer que seja o bloco executado, o resultado será um nome de
        usuário e uma saudação apropriada. Se essa for a primeira vez
        que o programa é executado, a saída será assim:
        What is your name? Eric
        We'll remember you when you come back, Eric!

        Caso contrário, será:
        Welcome back, Eric!

        Essa é a saída que você verá se o programa já foi executado pelo
        menos uma vez.
------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Salvando e lendo dados gerados pelo usuário (pg 250-252).

"""



import json

# Carrega o nome do usuário se foi armazenado anteriormente. Caso
# contrário, pede que o usuário forneça o nome e armazena essa
# informação.

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = input("- What is your name? ")

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)


    print("We'll remember you when you come back, " +
    username.title() + "!")

else:
    print("- Welcome back, " + username.title() + "!")
