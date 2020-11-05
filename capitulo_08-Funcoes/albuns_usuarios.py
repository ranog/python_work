#! /usr/bin/env python3

"""
NOME
    albuns_usuarios.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x albuns_usuarios.py
    ./albuns_usuarios.py

DESCRIÇÃO
    8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício
    8.7. Escreva um laço while que permita aos usuários fornecer o nome
    de um artista e o título de um álbum. Depois que tiver essas
    informações, chame make_album() com as entradas do usuário e
    apresente o dicionário criado. Lembre-se de incluir um valor de
    saída no laço while.

HISTÓRICO
    20200411: João Paulo, outubro de 2020.
        - 8.8 – Álbuns dos usuários (pg 182).

"""


def make_album(nome_artista, titulo_album, faixas = ''):
    albuns = {'artista' : nome_artista, 'album' : titulo_album,}

    if faixas:
        albuns['faixa'] = faixas

    # print(albuns)
    return albuns

"""
make_album('Pink Floyd', 'The Dark Side of the Moon')
make_album('Nirvana', 'Nevermind')
make_album('Metallica ', 'Metallica')
make_album('Red Hot Chili Peppers ', 'Californication', 6)
"""

while True:
    print("\n(Entre com 'q' a qualquer momento para sair)")

    n_artista = input("Nome do artista favorito: ")
    if n_artista.lower() == 'q':
        break

    t_album = input("Álbum favorito: ")
    if t_album.lower() == 'q':
        break

    artista = make_album(n_artista, t_album)

    print("\nDicionário:\n" + str(artista))
