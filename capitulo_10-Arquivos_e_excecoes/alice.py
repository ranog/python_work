#! /usr/bin/env python3

"""
NOME
    alice.py - Tratando a exceção FileNotFoundError.

SINOPSES
    chmod +x alice.py
    ./alice.py
    Sorry, the file alice.txt deos not exist.

------------------------------------------------------------------------

DESCRIÇÃO
    Python não é capaz de ler um arquivo ausente, portanto uma exceção é
    levantada: 
    
    Traceback (most recent call last): 
    File "alice.py", line 3, in <module> with open(filename) as f_obj:
    FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
    
    Nesse exemplo, o código no bloco try gera um FileNotFoundError,
    portanto Python procura um bloco except que trate esse erro. O
    interpretador então executa o código que está nesse bloco e o
    resultado é uma mensagem de erro simpática no lugar de um traceback.

------------------------------------------------------------------------

HISTÓRICO
    20202311: João Paulo, novembro de 2020.
        - Tratando a exceção FileNotFoundError (pg 243-244).

"""


filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.readtry

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " deos not exist."
    
    print(msg)
