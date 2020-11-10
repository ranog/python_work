#! /usr/bin/env python3

"""
NOME
    person.py - Devolvendo um dicionário.

SINOPSES
    chmod +x person.py
    ./person.py

    Devolvendo um dicionário:
    {'first': 'jimi', 'last': 'hendrix', 'age': 27}

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

    8.16 – Importações: Usando um programa que você tenha escrito e que
    contenha uma única função, armazene essa função em um arquivo
    separado.
    Importe a função para o arquivo principal de seu programa e chame-a
    usando cada uma das seguintes abordagens: 
    import nome_do_módulo
    from nome_do_módulo import nome_da_função
    from nome_do_módulo import nome_da_função as nf
    import nome_do_módulo as nm
    from nome_do_módulo import *

HISTÓRICO
    20200411: João Paulo, novembro de 2020.
        - Devolvendo um dicionário (pg 180-181).

    20201011: João Paulo, novembro de 2020.
        - 8.16 – Importações (pg 195).

"""


#import person_functions
#from person_functions import build_person
#from person_functions import build_person as bp
#import person_functions as pf
from person_functions import *

print("\nDevolvendo um dicionário: ")

# Chamada para import person_functions:
# musician = person_functions.build_person('jimi', 'hendrix', age = 27)

# Chamada para from person_functions import build_person:
#musician = build_person('jimi', 'hendrix', age = 27)

# Chamada para from person_functions import build_person as bp:
#musician = bp('jimi', 'hendrix', age = 27)

# Chamada para import person_functions as pf:
#musician = pf.build_person('jimi', 'hendrix', age = 27)

# Chamada para from person_functions import *: 
musician = build_person('jimi', 'hendrix', age = 27)

print(musician)
