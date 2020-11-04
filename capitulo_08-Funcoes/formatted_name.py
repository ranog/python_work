#! /usr/bin/env python3

"""
NOME
    formatted_name.py - Devolvendo um valor simples.

SINOPSES
    chmod +x formatted_name.py
    ./formatted_name.py

    Devolvendo um valor simples:
    Jimi Hendrix

    Deixando um argumento opcional:
    John Lee Hooker

DESCRIÇÃO
    A definição de get_formatted_name() aceita um primeiro nome e um
    sobrenome como parâmetros. A função combina esses dois nomes,
    acrescenta um espaço entre eles e armazena o resultado em full_name.
    O valor de full_name é convertido para que tenha letras iniciais
    maiúsculas e é devolvido para a linha que fez a chamada.
    Quando chamamos uma função que devolve um valor, precisamos fornecer
    uma variável em que o valor de retorno possa ser armazenado.
    Nesse caso, o valor devolvido é armazenado na variável musician.

    - Deixando um argumento opcional:

    O nome é criado a partir de três partes possíveis. Como o primeiro
    nome e o sobrenome sempre existem, esses parâmetros são listados
    antes na definição da função. O nome do meio é opcional, portanto é
    listado por último na definição, e seu valor default é uma string vazia.

HISTÓRICO
    20200411: João Paulo, novembro de 2020.
        - Devolvendo um valor simples. (pg 178).
        - Deixando um argumento opcional (pg 178-180).

"""


print("\nDevolvendo um valor simples: ")

def get_formatted_name(first_name, last_name, middle_name = ''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name

    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print("\nDeixando um argumento opcional: ")
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
