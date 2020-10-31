#! /usr/bin/env python3

"""
NOME
    while.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x while.py
    ./while.py

    - 7.4 - Ingredientes para uma pizza:

    Entre com os ingredientes de sua pizza:
    (Entre 'quit' se você quiser sair.) quit

    - 7.5 – Ingressos para o cinema:

    - Quantos anos você tem?
    (Entre com 'quit' para sair.) quit

    - 7.6 – Três saídas:

    CONDICIONAL:
    Entre com os ingredientes de sua pizza:
    (Entre 'quit' se você quiser sair.) quit

    ACTIVE:
    Entre com os ingredientes de sua pizza:
    (Entre 'quit' se você quiser sair.) quit

    BREAK:
    Entre com os ingredientes de sua pizza:
    (Entre 'quit' se você quiser sair.) quit

    - 7.7 – Infinito:
    1
    1
    1
    1
    1
    1
    ...

DESCRIÇÃO
    FAÇA VOCÊ MESMO

    7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao
    usuário para fornecer uma série de ingredientes para uma pizza até
    que o valor 'quit' seja fornecido. À medida que cada ingrediente é
    especificado, apresente uma mensagem informando que você
    acrescentará esse ingrediente à pizza.

    7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes
    para os ingressos de acordo com a idade de uma pessoa. Se uma pessoa
    tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver
    entre 3 e 12 anos, o ingresso custará 10 dólares; se tiver mais de
    12 anos, o ingresso custará 15 dólares. Escreva um laço em que você
    pergunte a idade aos usuários e, então, informe-lhes o preço do
    ingresso do cinema.

    7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do
    Exercício 7.5 que faça o seguinte, pelo menos uma vez:
    • use um teste condicional na instrução while para encerrar o laço;
    • use uma variável active para controlar o tempo que o laço
    executará;
    • use uma instrução break para sair do laço quando o usuário
    fornecer o valor 'quit'.

    7.7 – Infinito: Escreva um laço que nunca termine e execute-o. (Para
    encerrar o laço, pressione CTRL -C ou feche a janela que está
    exibindo a saída.)

HISTÓRICO
    20203010: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO (pg 163).

"""


print("\n- 7.4 - Ingredientes para uma pizza: ")

prompt = "\nEntre com os ingredientes de sua pizza: "
prompt += "\n(Entre 'quit' se você quiser sair.) "

while True:
    ingrediente = input(prompt)

    if ingrediente.lower() == 'quit':
        break

    else:
        print("Ingrediente " + ingrediente.title() + " adicionado na pizza.")

print("\n- 7.5 – Ingressos para o cinema: ")

active = True

prompt = "\n- Quantos anos você tem? "
prompt += "\n(Entre com 'quit' para sair.) "

while active:
    idade = input(prompt)

    if idade.lower() == 'quit':
        active = False

    elif int(idade) < 3:
        print("- Seu ingresso é gratuito.")

    elif int(idade) < 12:
        print("- Seu ingresso custa $10.")

    else:
        print("- Seu ingresso custa $15")

print("\n- 7.6 – Três saídas: ")


prompt = "\nEntre com os ingredientes de sua pizza: "
prompt += "\n(Entre 'quit' se você quiser sair.) "

ingrediente = ""

while ingrediente.lower() != 'quit':
    ingrediente = input("\nCONDICIONAL: " + prompt)
    if ingrediente.lower() != 'quit':
        print("Ingrediente " + ingrediente.title() + " adicionado na pizza.")

active = True

while active:
    item = input("\nACTIVE: " + prompt)

    if item.lower() == 'quit':
        active = False

    else:
        print("Ingrediente " + item + " adicionado na pizza.")

while True:
    item = input("\nBREAK: " + prompt)

    if item.lower() == 'quit':
        break

    else:
        print("Ingrediente " + item + " adicionado na pizza.")

print("\n- 7.7 – Infinito: ")

x = 1

while x < 10:
    # x += 1
    print(x)
