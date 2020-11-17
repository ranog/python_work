#! /usr/bin/env python3

"""
NOME
    my_electric_car.py - Armazenando várias classes em um módulo.

SINOPSES
    chmod +x my_electric_car.py
    ./my_electric_car.py
    2016 Tesla Model S
    This car has a 70-kWh battery.
    This car can go approximately 240 miles on a full charge.
    This car doesn't need a gas tank!

    This car has a 85-kWh battery.
    This car can go approximately 270 miles on a full charge.

    1990 Lamborghini Lm002
    Tank capacity is 290 L.

DESCRIÇÃO
    Esse código gera a mesma saída que vimos antes, embora a maior parte
    da lógica esteja oculta em um módulo.

HISTÓRICO
    20201611: João Paulo, novembro de 2020.
        - Armazenando várias classes em um módulo (pg 220-221).

"""


from car import Car, ElectricCar 

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()

print() 

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print()

my_car = Car('lamborghini', 'LM002', 1990)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
