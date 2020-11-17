#! /usr/bin/env python3

"""
NOME
    my_cars.py - Importando várias classes de um módulo.

SINOPSES
    chmod +x my_cars.py
    ./my_cars.py
    2016 Volkswagen Beetle
    2016 Tesla Roadster

DESCRIÇÃO
    Importe várias classes de um módulo separando cada classe com uma
    vírgula. Depois que importar as classes de que precisará, você
    poderá criar quantas instâncias de cada classe quantas forem
    necessárias.

HISTÓRICO
    20201711: João Paulo, novembro de 2020.
        - Importando várias classes de um módulo (pg 221).

"""


from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
