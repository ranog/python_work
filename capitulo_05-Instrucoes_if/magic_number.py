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

    - Testando várias condições:

    Usando and para testar várias condições:
    False
    True

    Usando or para testar várias condições:
    True
    False

DESCRIÇÃO
    O teste condicional passa porque o valor de answer (17) não é igual a 42.
    Como o teste passa, o bloco de código indentado é executado.

    Para verificar se duas condições são True simultaneamente, utilize a
    palavra reservada and para combinar os dois testes condicionais; se cada
    um dos testes passar, a expressão como um todo será avaliada como True.
    Se um dos testes falhar, ou ambos, a expressão será avaliada como False.

    A palavra reservada or permite verificar várias condições também, mas o
    teste passa se um dos testes individuais passar, ou ambos. Uma expressão
    or falha somente quando os dois testes individuais falharem.

----------------------------------------------------------------------

HISTÓRICO
    20201710: João Paulo, outubro de 2020.
        - Implementação da função para realizar comparações numéricas;
        - Usando and para testar várias condições;
        - Usando or para testar várias condições.

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

if age > 21:
    print("age > 21: " + str(age > 21))
else:
    print(age > 21)

if age >= 21:
    print("age >= 21: " + str(age >= 21))
else:
    print(age >= 21)

print("\n- Testando várias condições: ")

print("\nUsando and para testar várias condições: ")
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)

age_1 = 22

print(age_0 >= 21 and age_1 >= 21)

print("\nUsando or para testar várias condições: ")
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18

print(age_0 >= 21 or age_1 >= 21)
