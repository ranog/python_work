#! /usr/bin/env python3

"""
NOME
    car.py - Classe Car.

SINOPSES
    from car import Car

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

    - Modificando o valor de um atributo diretamente:

    Usamos a notação de ponto para acessar o atributo odometer_reading
    do carro e definir seu valor diretamente. Essa linha diz a Python
    para usar a instância my_new_car, encontrar o atributo
    odometer_reading associado a ela e definir o valor desse atributo
    com 23.

    - Modificando o valor de um atributo com um métoii:
    A úniii modificação em Car foi o acréscimo de update_odometer().
    Esse método aceita um valor de milhagem e o armazena em
    self.odometer_reading. Chamamos update_odometer() e lhe passamos o
    valor 23 como argumento (correspondendo ao parâmetro mileage na
    definição do método). Esse método define o valor de leitura do
    hodômetro com 23 e read_odometer() exibe essa leitura.

    Agora update_odometer() verifica se o novo valor do hodômetro faz
    sentido antes de modificar o atributo. Se a nova milhagem, mileage,
    for maior ou igual à milhagem existente, self.odometer_reading, você
    poderá atualizar o valor de leitura do hodômetro com a nova
    milhagem. Se a nova milhagem for menor que a milhagem existente,
    você receberá um aviso informando que não pode diminuir o valor lido
    no hodômetro.

    - Incrementando o valor de um atributo com um método:

    O novo método increment_odometer() aceita uma quantidade de milhas e
    soma esse valor a self.odometer_reading. Criamos um carro usado,
    my_used_car. Definimos seu hodômetro com o valor 23.500 chamando
    update_odometer() e passando-lhe o valor 23500. Chamamos
    increment_odometer() e passamos o valor 100 para somar as cem milhas
    que dirigimos entre comprar o carro e registrá-lo.

    - Importando uma única classe:

    Incluímos uma docstring no nível de módulo que descreve rapidamente
    o conteúdo desse módulo. Escreva uma docstring para cada módulo que
    criar.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - Classe Car (pg 205-206).
        - Definindo um valor default para um atributo (pg 206-207).

    20201311: João Paulo, novembro de 2020.
        - Modificando valores de atributos (pg 207-210).

    20201611: João Paulo, novembro de 2020.
        - Importando uma única classe (pg 218-219).

"""


"""Uma classe que pode ser usada para representar um carro.
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
