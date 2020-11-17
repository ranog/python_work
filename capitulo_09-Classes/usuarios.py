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
    Olá, Abrahão, obrigado por se cadastrar.

    - Logins: 10
    - Reset Logins: 0

    Cadastro do administrador do sistema:

    Nome completo: Johnny Ramnog
    Username: ranog
    e-mail: johnny@ranog.com.br
    Olá, Johnny, obrigado por se cadastrar.

    Lista de privilégios de administrador:
    - can add post
    - can delete post
    - can ban user

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


    9.11 – Importando Admin: Comece com seu programa do Exercício 9.8
    (página 241). Armazene as classes User, Privileges e Admin em um
    módulo. Crie um arquivo separado e uma instância de Admin e chame
    show_privileges() para mostrar que tudo está funcionando de forma
    apropriada.


    9.12 – Vários módulos: Armazene a classe User em um módulo e as 
    classes Privileges e Admin em um módulo separado. Em outro arquivo,
    crie uma instância de Admin e chame show_privileges() para mostrar
    que tudo continua funcionando de forma apropriada.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - 9.3 – Usuários (pg 204).

    20201311: João Paulo, novembro de 2020.
        - 9.5 – Tentativas de login (pg 210).

    20201711: João Paulo, novembro de 2020.
        - 9.11 – Importando Admin (pg 224).
        - 9.12 – Vários módulos (pg 224).
"""


from user import User
from privilegios import Privileges, Admin


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


print("\nCadastro do administrador do sistema: ")
root = Admin('johnny', 'ramnog','ranog', 'johnny@ranog.com.br')
root.describe_user()
root.greet_user()
root.privileges.show_privileges()
