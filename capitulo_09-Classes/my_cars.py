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

    - Importando um módulo completo:
    Importamos o módulo car inteiro. Então acessamos as classes
    necessárias por meio da sintaxe nome_do_módulo.nome_da_classe.
    Criamos novamente um Volkswagen Beetle e um Tesla Roadster.

    - Importando um módulo em um módulo:

    Importamos Car de seu módulo e ElectricCar de seu módulo. Em
    seguida, criamos um carro comum e um carro elétrico. Os dois tipos
    de carro são criados corretamente.

HISTÓRICO
    20201711: João Paulo, novembro de 2020.
        - Importando várias classes de um módulo (pg 221).
        - Importando um módulo completo (pg 221).
        - Importando um módulo em um módulo (pg 222-223).

"""


from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

"""
import car

my_beetle = car.Car('volkswagem', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
"""
