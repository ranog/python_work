#! /usr/bin/env python3

"""
NOME
    pizza.py - Uma lista em um dicionário.

SINOPSES
    chmod +x pizza.py
    ./pizza.py
    
    - Uma lista em um dicionário (pg 146-147).

    You ordered a thick-crust pizza with the following toppings:
        - mushrooms
        - extra cheese

DESCRIÇÃO
    Começamos com um dicionário que armazena informações sobre uma pizza
    que está sendo pedida. Uma das chaves do dicionário é 'crust', e o
    valor associado é a string 'thick'. A próxima chave, 'toppings',
    tem como valor uma lista que armazena todos os ingredientes
    solicitados. Resumimos o pedido antes de preparar a pizza. Para
    exibir os ingredientes, escrevemos um laço for. Para acessar a lista
    de ingredientes, usamos a chave 'toppings', e Python obtém a lista
    de ingredientes do dicionário.

------------------------------------------------------------------------

HISTÓRICO
    20202710: João Paulo, outubro de 2020.
        - Uma lista em um dicionário (pg 146-147).

"""


 # Armazena informações sobre uma pizza que está sendo pedida.

print("\n- Uma lista em um dicionário (pg 146-147).\n")

pizza = {'crust' : 'thick', 'toppings' : ['mushrooms', 'extra cheese'],}

# Resume o pedido
print("You ordered a " + pizza['crust'] +
      "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t- " + topping)
