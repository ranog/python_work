#! /usr/bin/env python3

"""
NOME
    car.py - Classe Car.

SINOPSES
    chmod +x car.py
    ./car.py
    2016 Audi A4
    This car has 0 miles on it.

DESCRIÇÃO
    Na classe Car definimos o método __init__() com o parâmetro self em
    primeiro lugar. 
    Também fornecemos outros três parâmetros: make, model e year. O
    método __init__() aceita esses parâmetros e os armazena nos
    atributos que serão associados às instâncias criadas a partir dessa
    classe. Quando criarmos uma nova instância de Car, precisaremos
    especificar um fabricante, um modelo e o ano para a nossa instância.
    Definimos um método chamado get_descriptive_name() que coloca os
    atributos year, make e model de um carro em uma string, descrevendo
    o carro de modo elegante. Isso evitará a necessidade de exibir o
    valor de cada atributo individualmente. Para trabalhar com os
    valores dos atributos nesse método, usamos self.make, self.model e
    self.year. Criamos uma instância da classe Car e a armazenamos na
    variável my_new_car. Então chamamos get_descriptive_name() para
    mostrar o tipo de carro.

    - Definindo um valor default para um atributo:

    Dessa vez, quando Python chama o método __init__() para criar uma
    nova instância, os valores para o fabricante, o modelo e o ano são
    armazenados como atributos, como fizemos no exemplo anterior. Em
    seguida, Python cria um novo atributo chamado odometer_reading e
    define seu valor inicial com 0. Também temos um novo método de nome
    read_odometer() que facilita a leitura da milhagem de um carro.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - Classe Car (pg 205-206).
        - Definindo um valor default para um atributo (pg 206-207).

"""


class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year

        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
