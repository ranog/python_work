#! /usr/bin/env python3

"""
NOME
    album.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x album.py
    ./album.py
    {'artista': 'Pink Floyd', 'album': 'The Dark Side of the Moon'}
    {'artista': 'Nirvana', 'album': 'Nevermind'}
    {'artista': 'Metallica ', 'album': 'Metallica'}

DESCRIÇÃO
    8.7 – Álbum: Escreva uma função chamada make_album() que construa um
    dicionário descrevendo um álbum musical. A função deve aceitar o
    nome de um artista e o título de um álbum e deve devolver um
    dicionário contendo essas duas informações. Use a função para criar
    três dicionários que representem álbuns diferentes. Apresente cada
    valor devolvido para mostrar que os dicionários estão armazenando as
    informações do álbum corretamente. Acrescente um parâmetro opcional
    em make_album() que permita armazenar o número de faixas em um
    álbum. Se a linha que fizer a chamada incluir um valor para o número
    de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
    menos uma nova chamada da função incluindo o número de faixas em um
    álbum.

HISTÓRICO
    20200411: João Paulo, outubro de 2020.
        - 8.7 – Álbum (pg 182).

"""


def make_album(nome_artista, titulo_album):
    albuns = {'artista' : nome_artista, 'album' : titulo_album}

    print(albuns)


make_album('Pink Floyd', 'The Dark Side of the Moon')
make_album('Nirvana', 'Nevermind')
make_album('Metallica ', 'Metallica')
