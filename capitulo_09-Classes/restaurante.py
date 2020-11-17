#! /usr/bin/env python3

"""
NOME
    restaurante.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x restaurante.py
    ./restaurante.py
    9.1 – Restaurante:

    Restaurante: Alcazar
    Culinária: Tradicional
    - Horário de funcionamento:
	    06:00-11:00
	    11:30-23:00

    9.4 – Pessoas atendidas:

    Restaurante: Bom Boi
    Culinária: Churrascaria
    - Foram atendidos 42 clientes.
    - Foram atendidos 13 clientes.
    - Atendemos 55 clientes em um dia de funcionamento.

DESCRIÇÃO
    9.1 – Restaurante: Crie uma classe chamada Restaurant.
    O método __init__() de Restaurant deve armazenar dois atributos:
    restaurant_name e cuisine_type. Crie um método chamado
    describe_restaurant() que mostre essas duas informações, e um
    método de nome open_restaurant() que exiba uma mensagem informando
    que o restaurante está aberto.
    Crie uma instância chamada restaurant a partir de sua classe. Mostre
    os dois atributos individualmente e, em seguida, chame os dois
    métodos.

    acesso ao site (11 de novembro de 2020):
        https://www.google.com/amp/s/viagemeturismo.abril.com.br/
        especiais/os-restaurantes-mais-classicos-de-sao-paulo-por
        -especialidade/amp/

    9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1
    (página 225). Acrescente um atributo chamado number_served cujo
    valor default é 0.
    Crie uma instância chamada restaurant a partir dessa classe.
    Apresente o número de clientes atendidos pelo restaurante e, em 
    seguida, mude esse valor e exiba-o novamente.
    Adicione um método chamado set_number_served() que permita definir o
    número de clientes atendidos. Chame esse método com um novo número e
    mostre o valor novamente.
    Acrescente um método chamado increment_number_served() que permita
    incrementar o número de clientes servidos. Chame esse método com
    qualquer número que você quiser e que represente quantos clientes
    foram atendidos, por exemplo, em um dia de funcionamento.

    9.10 – Importando Restaurant: Usando sua classe Restaurant mais
    recente, armazene-a em um módulo. Crie um arquivo separado que
    importe Restaurant.
    Crie uma instância de Restaurant e chame um de seus métodos para
    mostrar que a instrução import funciona de forma apropriada.

HISTÓRICO
    20201111: João Paulo, novembro de 2020.
        - 9.1 – Restaurante (pg 204).

    20201311: João Paulo, novembro de 2020.
        - 9.4 – Pessoas atendidas (pg 210).

    20201711: João Paulo, novembro de 2020.
        - 9.10 – Importando Restaurant (pg 223-224).

"""


import restaurant


print("\n9.1 – Restaurante: ")
restaurante = restaurant.Restaurant('alcazar', 'tradicional')

restaurante.describe_restaurant()
restaurante.open_restaurant()

print("\n9.4 – Pessoas atendidas: ")
restaurant = restaurant.Restaurant('bom boi', 'churrascaria')

restaurant.describe_restaurant()
#restaurant.number_served = 42
#restaurant.numero_clientes()
#restaurant.number_served = 13
#restaurant.numero_clientes()
restaurant.set_number_served(42)
restaurant.numero_clientes()
restaurant.set_number_served(13)
restaurant.numero_clientes()
restaurant.increment_number_served(42)
