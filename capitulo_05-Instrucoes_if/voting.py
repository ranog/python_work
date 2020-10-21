#! /usr/bin/env python3

"""
NOME
    voting.py - Instruções if

SINOPSES
    chmod +x voting.py
    ./voting.py


DESCRIÇÃO
    Instruções if simples

    Python verifica se o valor em age é maior ou igual a 18. É maior, portanto 
    a instrução indentada print em é executada: You are old enough to vote!

    O teste condicional passa e as duas instruções print estão indentadas,
    portanto ambas as linhas são exibidas:
    - You are old enough to vote!
    - Have you registered to vote yet?
    Se o valor de ageInstruçõesif-else for menor que 18, esse programa não
    apresentará nenhumasimplesi

    Instruções if-else

    Se o teste condicional passar, o primeiro bloco de instruções print
    indentadas será executado. Se o teste for avaliado como False, o bloco else
    será executado. Como age é menor que 18 dessa vez, o teste condicional
    falha e o código do bloco else é executado: Sorry, you are too young to
    vote.

    Sintaxe if-elif-else

    O teste if verifica se uma pessoa tem menos de 4 anos. Se o teste passar,
    uma mensagem apropriada será exibida e Python ignorará o restante dos
    testes. A linha elif, na verdade, é outro teste if, executado somente se o
    teste anterior falhar. Nesse ponto da cadeia, sabemos que a pessoa tem pelo
    menos 4 anos de idade, pois o primeiro teste falhou. Se a pessoa tiver
    menos de 18 anos, uma mensagem apropriada será exibida, e Python ignorará o
    bloco else. Se tanto o teste em if quanto o teste em elif falharem, Python
    executará o código do bloco else.

    As linhas em if-elif-else, definem o valor de price conforme a idade da
    pessoa, como no exemplo anterior. Depois que o preço é definido pela cadeia
    if-elif-else, uma instrução print separada e não indentada utiliza esse
    valor para exibir uma mensagem informando o preço de entrada da pessoa.

    Usando vários blocos elif

    O segundo bloco elif agora faz uma verificação para garantir que uma pessoa
    tenha menos de 65 anos antes de lhe cobrar o preço da entrada inteira, que
    é de 10 dólares. Observe que o valor atribuído no bloco else precisa ser
    alterado para 5 dólares, pois as únicas idades que chegam até esse bloco
    são de pessoas com 65 anos ou mais.

    Omitindo o bloco else

    O bloco elif extra atribui um preço de 5 dólares quando a pessoa tiver
    65 anos ou mais, o que é um pouco mais claro que o bloco else geral. Com
    essa mudança, todo bloco de código deve passar por um teste específico para
    ser executado.

----------------------------------------------------------------------

HISTÓRICO
    20202010: João Paulo, outubro de 2020.
        - Instruções if simples;
        - Instruções if-else;
        - Sintaxe if-elif-else;
        - Usando vários blocos elif;
        - Omitindo o bloco else;

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
age = 12

if age < 4: print("- Your admission cost is $0.")
elif age < 18: print("- Your admission cost is $5.")
else: print("- Your admission cost is $10.")

age = 20

if age < 4: price = 0
elif age < 18: price = 5

# Usando vários blocos elif
elif age < 65: price = 10

# Omitindo o bloco else
# else: price = 5
elif age >= 65: price = 5

print("\n- Your admission cost is $" + str(price))
