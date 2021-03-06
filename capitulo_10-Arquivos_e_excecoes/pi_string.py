#! /usr/bin/env python3

"""
NOME
    pi_string.py - Arquivos grandes: um milhão de dígitos.

SINOPSES
    chmod +x pi_string.py
    ./pi_string.py
    3.14159265358979323846264338327950288419716939937510...
    1000002

------------------------------------------------------------------------

DESCRIÇÃO
    - Arquivos grandes: um milhão de dígitos:
        A saída mostra que, realmente, temos uma string contendo pi com
        um milhão de casas decimais:
        3.14159265358979323846264338327950288419716939937510...
        1000002
        
        Seu aniversário está contido em pi (pg 236-237)?

        Enter your birthday, in the form mmddyy: 130820

        - Your birthday appears in the first million digits of pi!

        Python não tem nenhum limite inerente para a quantidade de dados
        com que podemos trabalhar; podemos trabalhar com tantos dados
        quantos a memória de seu sistema for capaz de tratar.


    - Seu aniversário está contido em pi (pg 236-237)?:

        Pedimos a data de nascimento do usuário e, em seguida,
        verificamos se essa string está em pi_string.

------------------------------------------------------------------------

HISTÓRICO
    20202011: João Paulo, novembro de 2020.
        - Arquivos grandes: um milhão de dígitos (pg 235-236).
        - Seu aniversário está contido em pi (pg 236-237)?

"""


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

print("\nSeu aniversário está contido em pi (pg 236-237)?")

birthday = input("\nEnter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("\n- Your birthday appears in the first million digits of pi!")

else:
    print("\n- Your birthday does not appear in the first million digits of pi.")
