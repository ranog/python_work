#! /usr/bin/env python3

"""
NOME
    many_users.py - Um dicionário emum dicionário.

SINOPSES
    chmod +x many_users.py
    ./many_users.py

    - Um dicionário em um dicionário.

    Username: aeinstein
        Full name: Albert Einstein
        Location: Princeton

    Username: mcurie
        Full name: Marie Curie
        Location: Paris

DESCRIÇÃO
    Inicialmente definimos um dicionário chamado users com duas chaves,
    uma para cada um dos seguintes nomes de usuário: 'aeinstein' e
    'mcurie'. O valor associado a cada chave é um dicionário que inclui
    o primeiro nome, o sobrenome e a localidade de cada usuário.
    Percorremos o dicionário users com um laço. Python armazena cada
    chave na variável username e o dicionário associado a cada nome de
    usuário na variável user_info. Depois que entrarmos no laço
    principal do dicionário, exibimos o nome do usuário.

------------------------------------------------------------------------

HISTÓRICO
    20202710: João Paulo, outubro de 2020.
        - Um dicionário em um dicionário (pg 148-149)

"""


print("\n- Um dicionário em um dicionário.")

users = {
    'aeinstein' : {'first' : 'albert', 'last': 'einstein',
    'location': 'princeton',},

     'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
