#! /usr/bin/env python3

"""
NOME
    user.py - FAÇA VOÇE MESMO.

SINOPSES
    from nome_do_módulo import nome_da_classe, nome_da_classe, ...

DESCRIÇÃO
    9.12 – Vários módulos: Armazene a classe User em um módulo e as
    classes Privileges e Admin em um módulo separado. Em outro arquivo,
    crie uma instância de Admin e chame show_privileges() para mostrar
    que tudo continua funcionando de forma apropriada.


HISTÓRICO
    20201711: João Paulo, novembro de 2020.
        - 9.12 – Vários módulos (pg 224).

"""


class User():
    """Um modelo simples de um perfil de usuário.
    """
    def __init__(self, first_name, last_name, username, email):
        """Inicializa os atrinutos dos usuários.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0


    def describe_user(self):
        """Resumo das informações do usuário.
        """
        print("\nNome completo: " + self.first_name.title() + " " +
              self.last_name.title())
        print("Username: " + self.username.lower())
        print("e-mail: " + self.email.lower())


    def greet_user(self):
        """Mostra uma saudação personalizada para o usuário.
        """
        print("Olá, " + self.first_name.title() + ", obrigado por se cadastrar.")


    def increment_login_attempts(self):
        """Incrementa o valor de login_attempts em 1.
        """
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts com 0.
        """
        self.login_attempts = 0
