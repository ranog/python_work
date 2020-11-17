#! /usr/bin/env python3

"""
NOME
    my_car.py - Importando uma únicaclasse.

SINOPSES
    chmod +x my_car.py
    ./my_car.py
    2016 Audi A4
    This car has 23 miles on it.
    This car has 46 miles on it.
    You can't roll back an odometer!

    2013 Subaru Outback
    This car has 23500 miles on it.
    This car has 23600 miles on it.

DESCRIÇÃO
    A instrução import diz a Python para abrir o módulo car e importar a
    classe Car. Agora podemos usar a classe Car como se ela estivesse
    definida nesse arquivo. A saída é a mesma que vimos antes.

HISTÓRICO
    20201611: João Paulo, novembro de 2020.
        - Importando uma única classe (pg 218-219).

"""


from car import Car

my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())

# Modificando o valor de um atributo diretamente:
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modificando o valor de um atributo com um método:
my_new_car.update_odometer(46)
my_new_car.read_odometer()

my_new_car.update_odometer(13)

print()
# Incrementando o valor de um atributo com um método:
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
