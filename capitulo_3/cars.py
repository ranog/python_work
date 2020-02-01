#! /usr/bin/env python3

"""
    NOME
        cars.py

    SINOPSES
        chmod +x lista_convidados.py
        ./cars.py

    DESCRIÇÃO
        Capítulo 3 Introdução às listas
            - Oraganizando uma lista.
            - Ordenando uma lista de forma permanente com o método 
            sort().
            - Ordenando uma lista temporariamente com a função 
            sorted().
         
-----------------------------------------------------------------------
    
    HISTÓRICO
        20203101: João Paulo, janeiro de 2020
            - Aplicação do método sort() para ordenar uma lista de 
            carros;
            - Uso do argumento reverse=True para ordenar a lista em 
            ordem inversa;
            - Aplicação da função sorted() para preservar a ordem 
            original de uma lista, mas apresentá-la de forma ordenada.
            
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
