#! /usr/bin/env python3

"""
NOME
    input.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x input.py
    ./input.py

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
