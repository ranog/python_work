#! /usr/bin/env python3

"""
NOME
    person.py - Devolvendo um dicionário.

SINOPSES
    chmod +x person.py
    ./person.py


DESCRIÇÃO
    A função build_person() aceita um primeiro nome e um sobrenome e
    então reúne esses valores em um dicionário. O valor de first_name é
    armazenado com a chave 'first' e o valor de last_name é armazenado
    com a chave 'last'. O dicionário completo que representa a pessoa é
    devolvido. O valor de retorno é exibido com as duas informações
    textuais originais agora armazenadas em um dicionário:
    {'first': 'jimi', 'last': 'hendrix'}

    Adicionamos um novo parâmetro opcional age à definição da função e
    atribuímos um valor default vazio ao parâmetro. Se a chamada da
    função incluir um valor para esse parâmetro, ele será armazenado no
    dicionário.
    Essa função sempre armazena o nome de uma pessoa, mas também pode
    ser modificada para guardar outras informações que você quiser sobre
    ela.

HISTÓRICO
    20200411: João Paulo, novembro de 2020.
    - Devolvendo um dicionário (pg 180-181).

"""


print("\nDevolvendo um dicionário: ")

def build_person(first_name, last_name, age = ''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first' : first_name, 'last' : last_name}

    if age:
        person['age'] = age

    return person

musician = build_person('jimi', 'hendrix', age = 27)

print(musician)
