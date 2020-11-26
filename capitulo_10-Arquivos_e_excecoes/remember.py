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

    - Refatoração

         A nova função get_stored_username() tem um propósito claro,
         conforme informado pela docstring. Essa função recupera um nome
         de usuário já armazenado e devolve esse nome se encontrar um.
         Se o arquivo username.json não existir, a função devolverá
         None. Essa é uma boa prática: uma função deve devolver o valor
         esperado ou None. Isso nos permite fazer um teste simples com o
         valor de retorno da função. Exibimos uma mensaguserE
         boas-vindas de volta ao usuário se a tentuserE de recuperar um
         nome foi bem-sucedida; caso contrário, pedimos que um novo nome
         de usuário seja fornecido.

        Cada função nessa última versão de remember.py tem um propósito
        único e claro. Chamamos greet_user() e essa função exibe uma
        mensagem apropriada: ela dá as boas-vindas de volta a um usuário
        existente ou saúda um novo usuário. Isso é feito por meio da
        chamada a get_stored_username(), que é responsável somente por
        recuperar um nome de usuário já armazenado, caso exista. Por
        fim, greet_user() chama get_new_username() se for necessário;
        essa função é responsável somente por obter um novo nome de
        usuário e armazená-lo. Essa separação do trabalho em
        compartimentos é uma parte essencial na escrita de um código
        claro, que seja fácil de manter e de estender.

------------------------------------------------------------------------

HISTÓRICO
    20202511: João Paulo, novembro de 2020.
        - Salvando e lendo dados gerados pelo usuário (pg 250-252).
        - Refatoração (pg 252-254).

"""



import json


def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""

    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("- What is your name? ")
    filename = 'username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username() 
    if username:
        print("- Welcome back, " + username.title() + "!")

    else:
        username = get_new_username()

        print("We'll remember you when you come back, " +
    username.title() + "!")


greet_user()
