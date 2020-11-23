#! /usr/bin/env python3

"""
NOME
    alice.py - Tratando a exceção FileNotFoundError.

SINOPSES
    chmod +x alice.py
    ./alice.py
    # Sorry, the file alice.txt deos not exist. 

    The file alice.txt has about 29461 words.

------------------------------------------------------------------------

DESCRIÇÃO
    - Tratando a exceção FileNotFoundError:
        Python não é capaz de ler um arquivo ausente, portanto uma
        exceção é levantada: 
    
        Traceback (most recent call last): 
        File "alice.py", line 3, in <module> with open(filename) as
        f_obj:
        FileNotFoundError: [Errno 2] No such file or directory:
        'alice.txt'
    
        Nesse exemplo, o código no bloco try gera um FileNotFoundError,
        portanto Python procura um bloco except que trate esse erro. O
        interpretador então executa o código que está nesse bloco e o
        resultado é uma mensagem de erro simpática no lugar de um
        traceback.


    - Analisando textos:

        Projeto Gutenberg (http://gutenberg.org/). O Projeto Gutenberg
        mantém uma coleção de obras literárias disponíveis em domínio
        público, e é um ótimo recurso se você estiver interessado em
        trabalhar com textos literários em seus projetos de programação.

        Movi o arquivo alice.txt para o diretório correto, portanto o
        bloco try funcionará dessa vez. Usamos a string contents, que
        agora contém todo o texto de Alice in Wonderland como uma string
        longa, e aplicamos o método split() para obter uma lista de
        todas as palavras do livro. Quando usamos len() nessa lista para
        verificar o seu tamanho, obtemos uma boa aproximação do número
        de palavras na string original. Exibimos uma frase que informa
        quantas palavras encontramos no arquivo. Esse código é colocado
        no bloco else porque funcionará somente se o código no bloco try
        for executado com sucesso. A saída nos informa quantas palavras
        estão em alice.txt

------------------------------------------------------------------------

HISTÓRICO
    20202311: João Paulo, novembro de 2020.
        - Tratando a exceção FileNotFoundError (pg 243-244).
        - Analisando textos (pg 244-245).

"""


filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " deos not exist."
    
    print(msg)

else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)

    print("\nThe file " + filename + " has about " + str(num_words) + " words.")
