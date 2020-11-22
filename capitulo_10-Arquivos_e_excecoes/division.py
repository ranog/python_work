#! /usr/bin/env python3

"""
NOME
    division.py - Tratando a exceção ZeroDivisionError.

SINOPSES
    chmod +x division.py
    ./division.py

    You can't divide by zero!

    Give me two numbers, and I'll divide them.
    - Enter 'q' to quit.

    First number: 5

    Second number: 0
    You can't divide by 0!

    First number: 5

    Second number: 2
    2.5

    First number: q

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


    - Usando exceções para evitar falhas:
        Esse programa pede que o usuário forneça um primeiro número
        (first_number) e, se o usuário não digitar q para sair, pede um
        segundo número (second_number). Então dividimos esses dois
        números para obter uma resposta (answer). O programa não faz
        nada para tratar erros, portanto pedir que uma divisão por zero
        seja feita causará uma falha no programa.

        O fato de o programa falhar é ruim, mas também não é uma boa
        ideia deixar que os usuários vejam os tracebacks. Usuários que
        não sejam técnicos ficarão confusos com eles e, em um ambiente
        malicioso, invasores aprenderão mais do que você quer que eles
        saibam a partir de um traceback. Por exemplo, eles saberão o
        nome de seu arquivo de programa e verão uma parte de seu código
        que não está funcionando de forma apropriada. Às vezes, um
        invasor habilidoso pode usar essas informações para determinar
        os tipos de ataque que podem usar contra o seu código.


    - Bloco else:
        Pedimos a Python para tentar concluir a operação de divisão em
        um bloco try, que inclui apenas o código que pode causar um
        erro. Qualquer código que dependa do sucesso do bloco try é
        adicionado no bloco else. Nesse caso, se a operação de divisão
        for bem-sucedida, usamos o bloco else para exibir o resultado.

        O bloco except diz como Python deve responder quando um
        ZeroDivisionError ocorrer. Se a instrução try não for
        bem-sucedida por causa de um erro de divisão por zero,
        mostraremos uma mensagem simpática informando o usuário de que
        modo esse tipo de erro pode ser evitado. O programa continua
        executando e o usuário jamais verá um traceback.

        O bloco try-except-else funciona assim: Python tenta executar o
        código que está na instrução try. O único código que deve estar
        em uma instrução try é aquele que pode fazer uma exceção ser
        levantada. Às vezes, você terá um código adicional que deverá
        ser executado somente se o bloco try tiver sucesso; esse código
        deve estar no bloco else. O bloco except diz a Python o que ele
        deve fazer, caso uma determinada exceção ocorra quando ele
        tentar executar o código que está na instrução try.

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - Tratando a exceção ZeroDivisionError (pg 240).
        - Usando blocos try-except (pg 241).
        - Usando exceções para evitar falhas (pg 241-242).
        - Bloco else (pg 242-243).

"""


try:
    print(5/0)

except ZeroDivisionError:
    print("\nYou can't divide by zero!")

print("\nGive me two numbers, and I'll divide them.")
print("- Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("\nSecond number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by 0!")

    else:
        print(answer)
