#! /usr/bin/env python3

"""
NOME
    magic_number.py - Comparações numéricas

SINOPSES
    chmod +x magic_number.py
    ./magic_number.py
    age = 18
    answer = 17

    - That is not the correct answer. Please try again!

    age == 18: True
    age < 21: True
    age <= 21: True
    False
    False

DESCRIÇÃO
    O teste condicional passa porque o valor de answer (17) não é igual a 42.
    Como o teste passa, o bloco de código indentado é executado.

----------------------------------------------------------------------

HISTÓRICO
    20201710: João Paulo, outubro de 2020.
        - Implementação da função para realizar comparações numéricas.

"""


age = 18
answer = 17

print("age = " + str(age))
print("answer = " + str(answer))

if answer != 42:
    print("\n- That is not the correct answer. Please try again!\n")

if age == 18:
    print("age == 18: " + str(age == 18))

if age < 21:
    print("age < 21: " + str(age < 21))

if age <= 21:
    print("age <= 21: " + str(age <= 21))

# Não é impresso porque os condicionais são False.
if age > 21:
    print("age > 21: " + str(age > 21))
else:
    print(age > 21)

if age >= 21:
    print("age >= 21: " + str(age >= 21))
else:
    print(age >= 21)
