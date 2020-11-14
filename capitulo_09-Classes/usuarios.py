#! /usr/bin/env python3

"""
NOME
    usuarios.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x usuarios.py
    ./usuarios.py

    Nome completo: Mario Schenberg
    Username: mschenberg
    e-mail: mario@schenberg.com.br
    Olá, Mario, obrigado por se cadastrar.

    Nome completo: Manoel Amoroso Costa
    Username: macosta
    e-mail: manoel@costa.com.br
    Olá, Manoel, obrigado por se cadastrar.

    Nome completo: Abrahão De Moraes
    Username: amores
    e-mail: abrahao@moraes.com.br
    Olá, Abrahão, obrigado por se cadastraii

    - Logins: 10
    - Reset Logins: 0

DESCRIÇÃO
    9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de
    nomes first_name e last_name e, então, crie vários outros atributos
    normalmente armazenados em um perfil de usuário. Escreva um método
    de nome describe_user() que apresente um resumo das informações do
    usuário. Escreva outro método chamado greet_user() que mostre uma
    saudação personalizada ao usuário.
    Crie várias instâncias que representem diferentes usuários e chame
    os dois métodos para cada usuário.

    9.5 – Tentativas de login: Acrescente um atributo chamado
    login_attempts à sua classe User do Exercício 9.3 (página 226).
    Escreva um método chamado increment_login_attempts() que incremente
    o valor de login_attempts em 1.
    Escreva outro método chamado reset_login_attempts() que reinicie o
    valor de login_attempts com 0.
    Crie uma instância da classe User e chame increment_login_attempts()
    várias vezes. Exiba o valor de login_attempts para garantir que ele
    foi incrementado de forma apropriada e, em seguida, chame
    reset_login_attempts(). Exiba login_attempts novamente para
    garantir que seu valor foi reiniciado com 0.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - 9.3 – Usuários (pg 204).

    20201311: João Paulo, novembro de 2020.
        - 9.5 – Tentativas de login (pg 210).

"""


class User():
    """Um modelo simples de um perfil de usuário.
    """
    def __init__(self, first_name, last_name, username, email):
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


usuario = User('mario', 'schenberg','mschenberg', 'mario@schenberg.com.br') 
usuario.describe_user()
usuario.greet_user()

usuario = User('manoel', 'amoroso costa','macosta', 'manoel@costa.com.br') 
usuario.describe_user()
usuario.greet_user()

usuario = User('abrahão', 'de moraes','amores', 'abrahao@moraes.com.br')
usuario.describe_user()
usuario.greet_user()

usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()

print("\n- Logins: " + str(usuario.login_attempts))

usuario.reset_login_attempts()
print("- Reset Logins: " + str(usuario.login_attempts))
