#! /usr/bin/env python3

"""
NOME
    word_count.py - Trabalhando com vários arquivos.

SINOPSES
    chmod +x word_count.py
    ./word_count.py

    The file alice.txt has about 29461 words.

    The file alice.txt has about 29461 words.

    The file moby_dick.txt has about 215136 words.

    The file little_women.txt has about 189079 words.

------------------------------------------------------------------------

DESCRIÇÃO
        A maior parte desse código não foi alterada. Simplesmente,
        indentamos o código e o movemos para o corpo de count_words().
        Manter os comentários atualizados é um bom hábito quando
        modificamos um programa; assim, transformamos o comentário em
        uma docstring e o alteramos um pouco.


    - Falhando silenciosamente:
        A única diferença entre essa listagem e a listagem anterior está
        na instrução pass. Agora, quando um FileNotFoundError é
        levantado, o código no bloco except é executado, mas nada
        acontece. Nenhum traceback é gerado e não há nenhuma saída em
        resposta ao erro levantado. Os usuários veem os contadores de
    palavras para cada arquivo existente, mas não há indicação sobre um
        arquivo não encontrado.

        A instrução pass também atua como um marcador. É um lembrete de
        que você optou por não fazer nada em um ponto específico da
        execução de seu programa, mas talvez queira fazer algo nesse
        local, no futuro. Por exemplo, nesse programa, podemos decidir
        escrever os nomes de qualquer arquivo ausente em um arquivo
        chamado missing_files.txt.
        Nossos usuários não verão esse arquivo, mas poderemos lê-lo e
        tratar qualquer texto ausente.

------------------------------------------------------------------------

HISTÓRICO
    20202311: João Paulo, novembro de 2020.
        - Trabalhando com vários arquivos (pg 245-246).

    20202411: João Paulo, novembro de 2020.
        - Falhando silenciosamente (pg 246-247).

"""


def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo.
    """

    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " deos not exist."
    
        #print(msg)
        pass

    else:
        # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)

        print("\nThe file " + filename + " has about " +
                str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
