#! /usr/bin/env python3

"""
NOME
    dados.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x dados.py
    ./dados.py
    
    - Dado de 6 lados:
    lance: 1 - lado: 4
    lance: 2 - lado: 1
    lance: 3 - lado: 4
    lance: 4 - lado: 2
    lance: 5 - lado: 4
    lance: 6 - lado: 3
    lance: 7 - lado: 4
    lance: 8 - lado: 5
    lance: 9 - lado: 2
    lance: 10 - lado: 1

    - Dado de 10 lados:
    lance: 1 - lado: 8
    lance: 2 - lado: 4
    lance: 3 - lado: 3
    lance: 4 - lado: 8
    lance: 5 - lado: 1
    lance: 6 - lado: 9
    lance: 7 - lado: 4
    lance: 8 - lado: 9
    lance: 9 - lado: 3
    lance: 10 - lado: 10

    - Dado de 20 lados:
    lance: 1 - lado: 4
    lance: 2 - lado: 11
    lance: 3 - lado: 6
    lance: 4 - lado: 16
    lance: 5 - lado: 6
    lance: 6 - lado: 14
    lance: 7 - lado: 17
    lance: 8 - lado: 5
    lance: 9 - lado: 7
    lance: 10 - lado: 15

DESCRIÇÃO
    9.14 – Dados: O módulo random contém funções que geram números
    aleatórios de várias maneiras. A função randint() devolve um inteiro
    no intervalo especificado por você. O código a seguir devolve um
    número entre 1 e 6:
    
    from random import randint 
    x = randint(1, 6)

    Crie uma classe Die com um atributo chamado sides, cujo valor
    default é 6.
    Escreva um método chamado roll_die() que exiba um número aleatório
    entre 1 e o número de lados do dado. Crie um dado de seis dados e
    lance-o dez vezes.
    Crie um dado de dez lados e outro de vinte lados. Lance cada dado
    dez vezes.

------------------------------------------------------------------------

HISTÓRICO
    20201811: João Paulo, novembro de 2020
        - 9.14 – Dados (pg 225).

"""


from random import randint


class Die():
    """Modelo simplificado de um dado.
    """
    def __init__(self, sides=6):
        """Inicialização dos atributos.
        """
        self.sides = sides


    def roll_die(self):
        """Exibe um número aleatório entre 1 e o número de lados do
        dado.
        """
        print("\n- Dado de " + str(self.sides) + " lados: ")

        jogada = 1
        while jogada <= 10:
            print("lance: " +
                  str(jogada) +
                  " - lado: " +
                  str(randint(1, self.sides)))
            jogada += 1


dado_6 = Die(6)
dado_6.roll_die()

dado_10 = Die(10)
dado_10.roll_die()

dado_20 = Die(20)
dado_20.roll_die()
