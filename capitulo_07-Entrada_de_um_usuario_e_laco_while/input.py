#! /usr/bin/env python3

"""
NOME
    input.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x input.py
    ./input.py
    7.1 – Locação de automóveis:
    - Qual tipo de carro gostaria de alugar? opala
    Deixe-me ver se consigo um Opala para você.

    7.2 – Lugares em um restauante:
    - Olá, mesa para quantas pessoa? 8
    Sua mesa está pronta.

    7.3 – Múltiplos de dez:
    - Entre com um número, por favor: 99
    O número 99 não é múltiplo de 10.

DESCRIÇÃO
    FAÇA VOCÊ MESMO pg 156.

HISTÓRICO
    20202910: João Paulo, outubro de 2020.
        FAÇA VOCÊ MESMO

        7.1 – Locação de automóveis: Escreva um programa que pergunte
        ao usuário qual tipo de carro ele gostaria de alugar. Mostre uma
        mensagem sobre esse carro, por exemplo, “Deixe-me ver se consigo
        um Subaru para você.”

        7.2 – Lugares em um restaurante: Escreva um programa que
        pergunte ao usuário quantas pessoas estão em seu grupo para
        jantar. Se a resposta for maior que oito, exiba uma mensagem
        dizendo que eles deverão esperar uma mesa. Caso contrário,
        informe que sua mesa está pronta.

        7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida,
        informe se o número é múltiplo de dez ou não.

"""

print("\n7.1 – Locação de automóveis: ")

carro = input("- Qual tipo de carro gostaria de alugar? ")

print("Deixe-me ver se consigo um " + carro.title() + " para você.")

print("\n7.2 – Lugares em um restauante: ")

grupo = input("- Olá, mesa para quantas pessoa? ")

grupo = int(grupo)

if grupo > 8:
    print("Desculpe-me mas não temos mesas vagas no momento. Favor aguardar.")

else:
    print("Sua mesa está pronta.")

print("\n7.3 – Múltiplos de dez: ")

number = input("- Entre com um número, por favor: ")

number = int(number)

if number % 10:
    print("O número " + str(number) + " não é múltiplo de 10.")

else:
    print("O número " + str(number): + " é um múltiplo de 10.")
