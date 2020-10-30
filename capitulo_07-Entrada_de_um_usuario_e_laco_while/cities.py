#! /usr/bin/env python3

"""
NOME
    cities.py - Usando break para sair de um laço.

SINOPSES
    chmod +x cities.py
    ./cities.py
    Please enter the name of a city you have visited:
    (Enter 'quit' when you are finished.) new york
    I'd love to go to New York!

    Please enter the name of a city you have visited:
    (Enter 'quit' when you are finished.) quit

DESCRIÇÃO
    Um laço que comece com while True executlaç indefinidamente, a menos
    que alcance uma instrução break.    O laço desse programa continuará
    pedindo aos usuários para que entrem com os nomes das cidades em que
    eles estiveram até que 'quit' seja fornecido. Quando 'quit' for
    digitado, a instrução break é executada, fazendo Python sair do
    laço.

------------------------------------------------------------------------

HISTÓRICO
    20203010: João Paulo, outubro de 2020.
        - Usando break para sair de um laço (pg 160-161).
"""



prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
