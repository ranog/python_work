#! /usr/bin/env python3

"""
NOME
    division.py - Tratando a exceção ZeroDivisionError.

SINOPSES
    chmod +x division.py
    ./division.py

    You can't divide by zero!

------------------------------------------------------------------------

DESCRIÇÃO
    - Tratando a exceção ZeroDivisionError:
        Traceback (most recent call last):
        File "./division.py", line 25, in <module>
            print(5/0)
        ZeroDivisionError: division by zero

        o shell devolveu 1

        O erro informado no traceback, ZeroDivisionError, é um objeto
        exceção. Python cria esse tipo de objeto em resposta a uma
        situação em que ele não é capaz de fazer o que lhe pedimos.
        Quando isso acontece, Python interrompe o programa e informa o
        tipo de exceção levantado.


    - Usando blocos try-except:
        Colocamos print(5/0) – a linha que causou o erro – em um bloco
        try. Se o código em um bloco try funcionar, Python ignorará o
        bloco except. Se o código no bloco try causar um erro, o
        interpretador procurará um bloco except cujo erro coincida com
        aquele levantado e executará o código desse bloco.

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - Tratando a exceção ZeroDivisionError (pg 240).
        - Usando blocos try-except (pg 241).

"""


try:
    print(5/0)

except ZeroDivisionError:
    print("\nYou can't divide by zero!")
