#! /usr/bin/env python3

"""
NOME
    electric_car.py - Método __init__() de uma classe-filha.

SINOPSES
    chmod +x electric_car.py
    ./electric_car.py
    2016 Tesla Model S

DESCRIÇÃO
    Começamos com Car. Quando criamos uma classe-filha, a classe-pai
    deve fazer parte do arquivo atual e deve aparecer antes da
    classe-filha no arquivo. Definimos a classe-filha, que é
    ElectricCar. O nome da classe-pai deve ser incluído entre
    parênteses na definição da classe-filha. O método __init__() aceita
    as informações necessárias para criar uma instância de Car.
    A função super() é uma função especial que ajuda Python a criar
    conexões entre a classe-pai e a classe-filha. Essa linha diz a
    Python para chamar o método __init__() da classe-pai de ElectricCar,
    que confere todos os atributos da classe-pai a ElectricCar. O nome
    super é derivado de uma convenção segundo a qual a classe-pai se
    chama superclasse e a classe-filha é a subclasse.
    Testamos se a herança está funcionando de forma apropriada tentando
    criar um carro elétrico com o mesmo tipo de informação que
    fornecemos quando criamos um carro comum. Criamos uma instância da
    classe ElectricCar e a armazenamos em my_tesla. Essa linha chama o
    método __init__() definido em ElectricCar que, por sua vez, diz a
    Python para chamar o método __init__() definido na classe-pai Car.
    Fornecemos os argumentos 'tesla', 'model s' e 2016.
    Além de __init__() não há outros atributos nem métodos que sejam
    particulares a um carro elétrico. A essa altura, estamos apenas
    garantindo que o carro elétrico tenha o comportamento apropriado de
    Car: 2016 Tesla Model S
    A instância de ElectricCar funciona exatamente como uma instância de
    Car, portanto podemos agora começar a definir atributos e métodos
    específicos aos carros elétricos.

HISTÓRICO
    20201411: João Paulo, novembro de 2020.
        - Método __init__() de uma classe-filha (pg 211-212).

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


    # Modificando o valor de um atributo com um método:
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor
        especificado. Rejeita a alteração se for tentativa de definir
        um valor menor para o hodômetro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    # Incrementando o valor de um atributo com um método
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do
        hodômetro."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos.
    """
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai.
        """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
