#! /usr/bin/env python3

"""
NOME
    usuarios.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x usuarios.py
    ./usuarios.py
Nome completo: MarioSchenberg
Username: mschenberg
e-mail: mario@schenberg.com.br
Olá, Mario, obrigado por se cadastrar.

Nome completo: ManoelAmoroso Costa
Username: macosta
e-mail: manoel@costa.com.br
Olá, Manoel, obrigado por se cadastrar.

Nome completo: AbrahãoDe Moraes
Username: amores
e-mail: abrahao@moraes.com.br
Olá, Abrahão, obrigado por se cadastrar.
DESCRIÇÃO
    9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de
    nomes first_name e last_name e, então, crie vários outros atributos
    normalmente armazenados em um perfil de usuário. Escreva um método
    de nome describe_user() que apresente um resumo das informações do
    usuário. Escreva outro método chamado greet_user() que mostre uma
    saudação personalizada ao usuário.
    Crie várias instâncias que representem diferentes usuários e chame
    os dois métodos para cada usuário.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - 9.3 – Usuários (pg 204).

"""


class User():
    """Um modelo simples de um perfil de usuário.1"""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        """Resumo das informações do usuário."""
        print("\nNome completo: " + self.first_name.title() +
              self.last_name.title())
        print("Username: " + self.username.lower())
        print("e-mail: " + self.email.lower())
    def greet_user(self):
        """Mostra uma saudação personalizada para o usuário."""
        print("Olá, " + self.first_name.title() + ", obrigado por se cadastrar.")

usuario = User('mario', 'schenberg','mschenberg', 'mario@schenberg.com.br') 
usuario.describe_user()
usuario.greet_user()

usuario = User('manoel', 'amoroso costa','macosta', 'manoel@costa.com.br') 
usuario.describe_user()
usuario.greet_user()

usuario = User('abrahão', 'de moraes','amores', 'abrahao@moraes.com.br')
usuario.describe_user()
usuario.greet_user()
