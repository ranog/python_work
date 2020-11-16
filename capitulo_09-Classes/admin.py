#! /usr/bin/env python3

"""
NOME
    admin.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x admin.py
    ./admin.py

    Nome completo: Mario Schenberg
    Username: mschenberg
    e-mail: mario@schenberg.com.br
    Olá, Mario, obrigado por se cadastrar.

    Lista de privilégios de administrador:
    - can add post
    - can delete post
    - can ban user

DESCRIÇÃO
    9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva
    uma classe chamada Admin que herde da classe User escrita no
    Exercício 9.3 (página 226), ou no Exercício 9.5 (página 232).
    Adicione um atributo privileges que armazene uma lista de strings
    como "can add post", "can delete post" "can ban user", e assim por
    diante. Escreva um método chamado show_privileges() que liste o
    conjunto de privilégios de um administrador. Crie uma instância de
    Admin e chame seu método.

HISTÓRICO
    20201611: João Paulo, novembro de 2020.
        - 9.7 – Admin (pg 217).

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


class Admin(User):
    """Modelo simplificado do usuário Admin.
        """
    def __init__(self, first_name, last_name, username, email):
        """Inicializa os atributos do usuário Admin.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """Lista o conjunto de privilégios de um administrador.
        """
        print("\nLista de privilégios de administrador: ")
        for self_privilege in self.privileges:
            print("- " + self_privilege)



root = Admin('mario', 'schenberg','mschenberg', 'mario@schenberg.com.br') 
root.describe_user()
root.greet_user()
root.show_privileges()
