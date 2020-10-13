#! /usr/bin/env python3

"""
    NOME
        cars.py

    SINOPSES
        chmod +x lista_convidados.py
        ./cars.py
        
            ['audi', 'bmw', 'subaru']
            ['subaru', 'bmw', 'audi']

            Here is the original list:
            ['bmw', 'audi', 'subaru']

            Here is the sorted list:
            ['audi', 'bmw', 'subaru']

            Here is the original list again:
            ['bmw', 'audi', 'subaru']

            Método reverse():
            ['bmw', 'audi', 'toyota', 'subaru']
            ['subaru', 'toyota', 'audi', 'bmw']

            Função len(): 4

    DESCRIÇÃO
        Capítulo 3 Introdução às listas
            - Oraganizando uma lista.
            - Ordenando uma lista de forma permanente com o método 
            sort().
            - Ordenando uma lista temporariamente com a função 
            sorted().
            - Exibindo uma lista em ordem inversa.
            - Descobrindo o tamanho de uma lista.

-----------------------------------------------------------------------
    
    HISTÓRICO
        20203101: João Paulo, janeiro de 2020
            - Aplicação do método sort() para ordenar uma lista de 
            carros;
            - Uso do argumento reverse=True para ordenar a lista em 
            ordem inversa;
            - Aplicação da função sorted() para preservar a ordem 
            original de uma lista, mas apresentá-la de forma ordenada.
            
        20200402: João Paulo, fevereiro de 2020
            - Aplicação do método reverse().
            - Usando a função len() para descobrir o tamanho de uma 
            lista.
"""

cars = ["bmw", "audi", "subaru"]

cars.sort()
print(cars)

# Ordem alfabética inversa
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "subaru"]
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
# Essa função também pode aceitar um argumento reverse=True se 
# quiser exibir uma lista em ordem inversa.

print("\nHere is the original list again:")
print(cars)

print("\nMétodo reverse():")

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(cars)

# O método reverse() muda a ordem de uma lista de forma permanente.

print("\nFunção len(): " + str(len(cars)))
