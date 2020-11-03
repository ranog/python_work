#! /usr/bin/env python3

"""
NOME
    pets.py - Argumentos posicionais.

SINOPSES
    chmod +x pets.py
    ./pets.py

DESCRIÇÃO
    - Argumentos posicionais:

    A definição mostra que essa função precisa de um tipo de animal e de
    seu nome. Quando chamamos describe_pet(), devemos fornecer o tipo do
    animal e um nome, nessa ordem. Por exemplo, na chamada da função, o
    argumento 'hamster' é armazenado no parâmetro animal_type e o
    argumento 'harry' é armazenado no parâmetro pet_name. No corpo da
    função, esses dois parâmetros são usados para exibir informações
    sobre o animal de estimação descrito.

    - Várias chamadas de função:

    Nessa segunda chamada da função, passamos os argumentos 'dog' e
    'willie' a describe_pet(). Assim como no conjunto anterior de
    argumentos que usamos, Python faz a correspondência entre 'dog' e o
    parâmetro animal_type e entre 'willie' e o parâmetro pet_name. Como
    antes, a função faz sua tarefa, porém, dessa vez, exibe valores para
    um cachorro chamado Willie.

    Chamar uma função várias vezes é uma maneira eficiente de trabalhar.

    - A ordem é importante em argumentos posicionais:

    Nessa chamada de função, listamos primeiro o nome e depois o tipo do
    animal. Como dessa vez o argumento 'harry' foi definido antes, esse
    valor é armazenado no parâmetro animal_type. De modo semelhante,
    'hamster' é armazenado em pet_name. Agora temos um "harry" chamado
    "Hamster".

    - Argumentos nomeados:

    A função describe_pet() não mudou. Entretanto, quando chamamos a
    função, dizemos explicitamente a Python a qual parâmetro cada
    argumento deve corresponder. Quando Python lê a chamada da função,
    ele sabe que deve armazenar o argumento 'hamster' no parâmetro
    animal_type e o argumento 'harry' em pet_name. A saída mostra
    corretamente que temos um hamster chamado Harry.

HISTÓRICO
    20200211: João Paulo, outubro de 2020.
        - Argumentos posicionais (pg 172).
        - Várias chamadas de função (pg 172-173).
        - A ordem é importante em argumentos posicionais (pg 173).

    20200311: João Paulo, novembro de 2020.
        - Argumentos nomeados (pg 173-174).

"""


"""Exibe informações sobre um animal de estimação."""
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#XXX A orem é importante em argumentos posicionais:
describe_pet('harry', 'hamster')

"""Quando usar argumentos nomeados, lembre-se de usar os nomes exatos
dos parâmetros usados na definição da função."""

print("\n- Argumentos nomeados: ")
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
