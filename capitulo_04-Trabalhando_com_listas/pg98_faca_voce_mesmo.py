#! /usr/bin/env python3

"""
NOME
    pg98_faca_voce_mesmo.py

SINOPSES
    chmod +x pg98_faca_voce_mesmo.py
    ./pg98_faca_voce_mesmo.py

DESCRIÇÃO
    FAÇA VOCÊ MESMO

    4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
    incluindo-os.

    4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
    laço for para exibir os números. (Se a saída estiver demorando demais,
    interrompa pressionando CTRL -C ou feche a janela de saída.)

    4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em
    seguida, use min() e max() para garantir que sua lista realmente começa em um
    e termina em um milhão. Além disso, utilize a função sum() para ver a rapidez
    com que Python é capaz de somar um milhão de números.

    4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
    uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
    os números.

    4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
    exibir os números de sua lista.

    4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
    exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
    primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
    para exibir o valor de cada cubo.

    4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
    dos dez primeiros cubos.

----------------------------------------------------------------------

HISTÓRICO
    20201310: João Paulo, outubro de 2020.
        - Implementação do exercício 4.3 - Contando até vinte;
        - Implementação do exercício 4.4 - Um milhão;
        - Implementação do exercício 4.5 - Somando um milhão;
        - Implementação do exercício 4.6 - Números ímpares;
        - Implementação do exercício 4.7 - Três;
        - Implementação do exercício 4.8 – Cubos;
        - Implementação do exercício 4.9 – Comprehension de cubos.
"""


print("4.3 - Contando até vinte: ")

for count in range(1, 21):
    print(count)

print("\n4.4 – Um milhão: ")
for number in range(1, 1001):
    print(number)

print("\n4.5 – Somando um milhão: ")
numbers = list(range(1, 1001))
print("Valor mínimo: " + str(min(numbers)))
print("Valor máximo: " + str(max(numbers)))
print("Soma: " + str(sum(numbers)))

print("\n4.6 – Números ímpares: ")
for impar in range(1, 21, 2):
    print(impar)

print("\n4.7– Três: ")
for multiplo in range(3, 31, 3):
    print(multiplo)

print("\n4.8 – Cubos: ")
cubos = []
for cubo in range(1, 11):
    cubos.append(cubo ** 3)

print(cubos)

print("\n4.9 – Comprehension de cubos: ")
cubos_comprehension = [cubo**3 for cubo in range(1,11)]
print(cubos_comprehension)
