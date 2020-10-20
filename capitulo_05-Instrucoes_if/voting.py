#! /usr/bin/env python3

"""
NOME
    voting.py - Instruçõesif simples

SINOPSES
    chmod +x voting.py
    ./voting.py


DESCRIÇÃO
    Instruções if simples

    Python verifica se o valor em age é maior ou igual a 18. É maior, portanto a instrução indentada print em é executada: You are old enough to vote!

    O teste condicional passa e as duas instruções print estão indentadas, portanto ambas as linhas são exibidas: 
    - You are old enough to vote!
    - Have you registered to vote yet?
    Se o valor de ageInstruçõesif-else for menor que 18, esse programa não apresentará nenhumasimplesi

    Instruções if-else

    Se o teste condicional passar, o primeiro bloco de instruções print indentadas será executado. Se o teste for avaliado como False, o bloco else será executado. Como age é menor que 18 dessa vez, o teste condicional falha e o código do bloco else é executado: Sorry, you are too young to vote.

----------------------------------------------------------------------

HISTÓRICO
    20202010: João Paulo, outubro de 2020.
        - Instruções if simples;
        - Instruções if-else;
        - Sintaxe if-elif-else;

"""

print("\nInstruções if simples:")
age = 19

if age >= 18:
    print("- You are old enough to vote!")
    print("- Have you registered to vote yet?")

print("\nInstruções if-else:")
age = 17

if age >= 18:
    print("- You are old enough to vote!")
    print("- Have you registered to vote yet?")

else:
    print("- Sorry, you are too young to vote.") 
    print("- Please register to vote as soon as you turn 18!")

print("\nSintaxe if-elif-else:")
