#! /usr/bin/env python3

"""
NOME
    electric_car.py - Método __init__() de uma classe-filha.

SINOPSES
    chmod +x electric_car.py
    ./electric_car.py
    
    2016 Tesla Model S
    This car has a 70-kWh battery.
    This car doesn't need a gas tank!
    This car can go approximately 240 miles on a full charge.

    This car has a 85-kWh battery.
    This car can go approximately 270 miles on a full charge.

    1990 Lamborghini Lm002
    Tank capacity is 290 L.

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

    - Definindo atributos e métodos da classe-filha:

    Adicionamos um novo atributo self.battery_size e definimos seu valor
    inicial, por exemplo, com 70. Esse atributo será associado a todas
    as instâncias criadas a partir da classe ElectricCar, mas não será
    associado a nenhuma instância de Car. Também adicionamos um método
    chamado describe_battery(), que exibe informações sobre a bateria.
    Quando chamamos esse método, temos uma descrição que é claramente
    específica de um carro elétrico.

    Um atributo ou método que possa pertencer a qualquer carro, isto é,
    que não seja específico de um carro elétrico, deve ser adicionado à
    classe Car , em vez de ser colocado na classe ElectricCar.
    Então qualquer pessoa que usar a classe Car terá essa funcionalidade
    disponível também, e a classe ElectricCar conterá apenas códigos
    para as informações e comportamentos específicos de veículos
    elétricos.

    - Instâncias como atributos:

    Definimos uma nova classe chamada Battery que não herda de nenhuma
    outra classe. O método __init__() tem um parâmetro, battery_size,
    além de self. É um parâmetro opcional que define a capacidade da
    bateria com 70 se nenhum valor for especificado. O método
    describe_battery() também foi transferido para essa classe.
    Na classe ElectricCar, adicionamos um atributo chamado self.battery.
    Essa linha diz a Python para criar uma nova instância de Battery
    (com capacidade default de 70, pois não estamos especificando nenhum
    valor) e armazenar essa instância no atributo self.battery. Isso
    acontecerá sempre que o método __init__() for chamado; qualquer
    instância de ElectricCar agora terá uma instância de Battery criada
    automaticamente.
    Criamos um carro elétrico e o armazenamos na variável my_tesla.
    Quando quisermos descrever a bateria, precisaremos trabalhar com o
    atributo battery do carro: my_tesla.battery.describe_battery() Essa
    linha diz a Python para usar a instância my_tesla, encontrar seu
    atributo battery e chamar o método describe_battery() associado à
    instância de Battery armazenada no atributo.
    A saída é idêntica àquela que vimos antes.

    O novo método get_range() efetua uma análise simples. Se a
    capacidade da bateria for de 70 kWh, get_range() define o alcance do
    carro com 240 milhas; se a capacidade for de 85 kWh, o alcance será
    definido com 270 milhas. Esse valor é então apresentado. Quando
    quisermos usar esse método, novamente, devemos chamá-lo por meio do
    atributo battery do carro.

    9.9 – Upgrade de bateria: Use a última versão de electric_car.py
    desta seção.
    Acrescente um método chamado upgrade_battery() na classe Battery.
    Esse método deve verificar a capacidade da bateria e defini-la com
    85 se o valor for diferente. Crie um carro elétrico com uma
    capacidade de bateria default, chame get_range() uma vez e, em
    seguida, chame get_range() uma segunda vez após fazer um upgrade da
    bateria. Você deverá ver um aumento na distância que o carro é capaz
    de percorrer.

HISTÓRICO
    20201411: João Paulo, novembro de 2020.
        - Método __init__() de uma classe-filha (pg 211-212).
        - Definindo atributos e métodos da classe-filha (pg 212-213).

    20201511: João Paulo, novembro de 2020.
        - Sobrescrevendo métodos da classe-pai (pg 214).
        - Instâncias como atributos (pg 214-216).

    20201611: João Paulo, novembro de 2020.
        - 9.9 – Upgrade de bateria (pg 218).

    20201711: João Paulo, novembro de 2020.
        - Importando um módulo em um módulo. (pg 222-223).

"""


"""Um conjunto de classes que pode ser usado para representar carros
elétricos.
"""

from car import Car

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico.
    """
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria.
        """
        self.battery_size = battery_size


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de
        percorrer com essa bateria.
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."

        print(message)


    def upgrade_battery(self):
        """Verificar a capacidade da bateria e defini com 85 se o valor
        for diferente.
        """
        if self.battery_size != 85:
            self.battery_size = 85
        

class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos.
    """
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai. Em seguida, inicializa
        os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina.
        """
        print("This car doesn't need a gas tank!")
