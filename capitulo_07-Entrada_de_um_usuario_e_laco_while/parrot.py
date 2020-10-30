#! /usr/bin/env python3

"""
NOME
    parrot.py - Como afunção input() trabalha.

SINOPSES
    chmod +x parrot.py
    ./parrot.py

    Tell me something, and I will repeat it back to you:Hello everyone!
    Hello everyone!

DESCRIÇÃO
    O programa espera enquanto o usuário fornece sua resposta e continua
    depois que ele tecla ENTER. A resposta é armazenada na variável.

    - Deixando o usuário decidir quando quer sair:

    Definimos um prompt que informa quais são as duas opções ao usuário:
    fornecer uma mensagem ou o valor de saída (nesse caso, é 'quit'). Em
    seguida, preparamos uma variável message para armazenar o valor que
    o usuário fornecer. Definimos message como uma string vazia, "", de
    modo que Python tenha algo para conferir na primeira vez que
    alcançar a linha com while. Na primeira vez que o programa executar
    e Python alcançar a instrução while, ele deverá comparar o valor de
    message com 'quit', mas o usuário ainda não forneceu nenhuma
    entrada. Se Python não tiver nada para comparar, ele não será capaz
    de continuar executando o programa. Para resolver esse problema,
    garantimos que message receba um valor inicial. Embora seja apenas
    uma string vazia, ela fará sentido para Python e permitirá que a
    comparação que faz o laço while funcionar seja feita. Esse laço
    while executa enquanto o valor de message não for 'quit'.

    Agora o programa faz uma verificação rápida antes de mostrar a
    mensagem e só a exibirá se ela não for igual ao valor de saída.

------------------------------------------------------------------------

HISTÓRICO
    20202810: João Paulo, outubro de 2020.
        - Como afunção input() trabalha (pg 152-153).

    20202910: João Paulo, outubro de 2020.
        - Deixando o usuário decidir quando quer sair (pg 157-158).

"""


print("\n- Como afunção input() trabalha: ")
message = input("Tell me something, and I will repeat it back to you: ")

print(message)

print("\n- Deixando o usuário decidir quando quer sair: ")

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
