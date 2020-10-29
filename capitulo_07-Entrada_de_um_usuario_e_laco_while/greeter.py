#! /usr/bin/env python3

"""
NOME
    greeter.py - Escrevendo prompts claros.

SINOPSES
    chmod +x greeter.py
    ./greeter.py
    Please enter your name: Eric
    - Hello, Eric!

    If you tell us who you are, we can personalize the messages you see.
    What is your first name? John
    - Hello, John!

DESCRIÇÃO
    Sempre que usar a função input(), inclua um prompt claro, fácil de
    compreender, que informe o usuário exatamente que tipo de informação
    você procura. Qualquer frase que diga aos usuários o que eles devem
    fornecer será apropriada.

    Você pode armazenar seu prompt em uma variável e passá-la para a
    função input(). Isso permite criar seu prompt com várias linhas e
    escrever uma instrução input() clara.

------------------------------------------------------------------------

HISTÓRICO
    20202810: João Paulo, outubro de 2020.
        - Escrevendo prompts claros (pg 153-154).

"""


name = input("Please enter your name: ")


""" 
    Esse exemplo mostra uma maneira de criar uma string multilinha. A
    primeira linha armazena a parte inicial da mensagem na variável
    prompt. Na segunda linha, o operador += acrescenta a nova string no
    final da string que estava armazenada em prompt.
"""

prompt = "\nIf you tell us who you are, we can personalize the messages you see."

prompt += "\nWhat is your first name? "

name = input(prompt)

print("- Hello, " + name.title() + "!")
