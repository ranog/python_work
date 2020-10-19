#! /usr/bin/env python3

"""
NOME
    testes_condicionais.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x testes_condicionais.py
    ./testes_condicionais.py


DESCRIÇÃO
    5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba
    uma frase que descreva o teste e o resultado previsto para cada um. Seu
    código deverá ser semelhante a:

    car = 'subaru'

    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    • Observe atentamente seus resultados e certifique-se de que compreende por
    que cada linha é avaliada como True ou False.
    • Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como
    True e outros cinco avaliados como False.

    5.2 – Mais testes condicionais: Você não precisa limitar o número de testes
    que criar em dez. Se quiser testar mais comparações, escreva outros teste5.2 – Mais testes condicionaiss
    e acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True
    e um False para cada um dos casos a seguir:

    • testes de igualdade e de não igualdade com strings;
    • testes usando a função lower();
    • testes numéricos que envolvam igualdade e não igualdade, maior e menor
    que, maior ou igual a e menor ou igual a;
    • testes usando as palavras reservadas and e or;
    • testes para verificar se um item está em uma lista;
    • testes para verificar se um item não está em uma lista.

----------------------------------------------------------------------

HISTÓRICO
    20201810: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO
            - 5.1 – Testes condicionais;
            - 5.2 – Mais testes condicionais.

"""


print("5.1 – Testes condicionais:")

car = 'subaru'
young = 18
old = 74

print("\n- Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n- Young == 18? I predict True.")
print(young == 18)

print("\n- Young <= 18? I predict True." )
print(young <= 18)

print("\n- Young >= 18? I predict True.")
print(young >= 18)

print("\n- Young >= 18 and Old <= 74? I predict True.")
print(young >= 18 and old <= 74)

print("\n- Is car == 'audi'? I predict False.")
print(car == 'audi')

print("\n- Young < 18? I predict False.")
print(young < 18)

print("\n- Old > 74? I predict False." )
print(young > 74)

print("\n- Young > 18? I predict False.")
print(young > 18)

print("\n- Young > 18 or Old > 74? I predict False.")
print(young > 18 or old > 74)

print("\n5.2 – Mais testes condicionais:")

print("\n- Testes de igualdade e de não igualdade com strings:")

nome = 'Silva'
sobrenome = 'silva'

print("\nnome == Silva?")
print(nome == 'Silva')

print("\nnome == silva?")
print(nome == 'silva')

print("\n- Testes usando a função lower():")

print("\n" + nome + " == " + sobrenome + " (sem a função lower())?")
print(nome == sobrenome)

print("\n" + nome + " == " + sobrenome + " (com a função lower())?")
print(nome.lower() == sobrenome)

print("\n- Testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a:")

answer = 42

print("\nanswer == 42?")
print(answer == 42)
print("\nanswer != 42?")
print(answer != 42)

