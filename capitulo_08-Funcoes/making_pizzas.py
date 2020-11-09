#! /usr/bin/env python3

"""
NOME
    making_pizzas.py - Importando ummódulo completo.

SINOPSES
    chmod +x making_pizzas.py
    ./making_pizzas.py

    Making a 16-inch pizza with the following toppings:
    - pepperoni

    Making a 12-inch pizza with the following toppings:
    - mushrooms
    - green peppers
    - extra cheese

DESCRIÇÃO
    Um módulo é um arquivo terminado em .py que contém o código que
    queremos importar para o nosso programa. Vamos criar um módulo que
    contenha a função make_pizza().
    Para criar esse módulo, removeremos tudo que está no arquivo
    pizza.py, exceto a função make_pizza().

    Agora criaremos um arquivo separado chamado making_pizzas.py no
    mesmo diretório em que está pizza.py. Esse arquivo importa o módulo
    que acabamos de criar e, em seguida, faz duas chamadas para make_pizza().

    Quando Python lê esse arquivo, a linha import pizza lhe diz para
    abrir o arquivo pizza.py e copiar todas as funções dele para esse
    programa. Você não vê realmente o código sendo copiado entre os
    arquivos porque Python faz isso internamente, à medida que o
    programa executa. Tudo que você precisa saber é que qualquer função
    definida em pizza.py agora estará disponível em making_pizzas.py.

    - Importando funções específicas:

    from nome_do_módulo import nome_da_função Você pode importar quantas
    funções quiser de um módulo separando o nome de cada função com uma
    vírgula: from nome_do_módulo import função_0, função_1, função_2.

HISTÓRICO
    20200811: João Paulo, novembro de 2020.
        - Importando um módulo completo (pg 191-192).

    20200911: João Paulo, novembro de 2020.
        - Importando funções específicas (pg 192).

"""


# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
