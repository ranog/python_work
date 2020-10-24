#! /usr/bin/env python3

"""
NOME
    favorite_languages.py - Um dicionário de objetos semelhantes

SINOPSES
    chmod +x favorite_languages.py
    ./favorite_languages.py

    - Sarah's favorite language is C.

DESCRIÇÃO
    - Um dicionário de objetos semelhantes

    Quando souber que precisará de mais de uma linha para definir um dicionário,
    tecle ENTER depois da chave de abertura. Em seguida, indente a próxima linha
    em um nível (quatro espaços) e escreva o primeiro par chave-valor, seguido
    de uma vírgula. A partir desse ponto, quando pressionar ENTER , seu editor
    de texto deverá indentar automaticamente todos os pares chave-valor
    subsequentes para que estejam de acordo com o primeiro par chave-valor.

    Depois que acabar de definir o dicionário, acrescente uma chave de fechamento
    em uma nova linha após o último par chave-valor e indente-a em um nível para
    que esteja alinhada com as chaves do dicionário. Incluir uma vírgula após o
    último par chave-valor também é uma boa prática; assim você estará preparado
    para acrescentar um novo par chave-valor na próxima linha.

    A palavra print é menor que a maioria dos nomes de dicionário, portanto faz
    sentido incluir a primeira parte do que você quer exibir logo depois do
    parêntese de abertura. Escolha um ponto apropriado para separar o que está
    sendo exibido e acrescente um operador de concatenação ( + ) no final da
    primeira linha. Tecle ENTER e depois TAB para alinhar todas as linhas
    subsequentes em um nível de indentação abaixo da instrução print . Quando
    terminar de compor sua saída, você pode colocar o parêntese de fechamento
    na última linha do bloco print.

----------------------------------------------------------------------

HISTÓRICO
    20202310: João Paulo, outubro de 2020.
        - Um dicionário de objetos semelhantes - Pag. 136-137.

"""


favorite_languages = { 'jen' : 'python',
                       'sarah' : 'c',
                       'edward' : 'ruby',
                       'phil' : 'python',}

# Essa sintaxe é usada na instrução print em v, e a saída mostra a linguagem
# predileta de Sarah:
print("\n- Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
