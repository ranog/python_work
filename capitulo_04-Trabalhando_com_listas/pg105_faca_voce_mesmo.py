#! /usr/bin/env python3

"""
NOME
    pg105_faca_voce_mesmo.py

SINOPSES
    chmod +x pg105_faca_voce_mesmo.py
    ./pg105_faca_voce_mesmo.py

DESCRIÇÃO
    4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
    de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
    • Use um laço for para exibir cada prato oferecido pelo restaurante.
    • Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
    • O restaurante muda seu cardápio, substituindo dois dos itens com pratos
    diferentes. Acrescente um bloco de código que reescreva a tupla e, em
    seguida, use um laço for para exibir cada um dos itens do cardápio
    revisado.

----------------------------------------------------------------------

HISTÓRICO
    20201610: João Paulo, outubro de 2020.
        - Implementação do exercício 4.13 - Buffet.

"""

pratos = ('café colonial', 'comidas típicas das festas de são joão', 'carne de sol maracaípe', 'camarão havaiano maracaípe', 'torresmim')

print("4.13 – Buffet:")
for prato in pratos:
    print("- " + prato.title())

# XXX pratos[0] = 'empadão'     TypeError
# XXX pratos.append('empadão')  TypeError

print("\nTupla: " + str(pratos))

pratos = ('café colonial', 'empadão', 'carne de sol maracaípe', 'dormência', 'torresmim')

print("\n4.13 – Buffet (revisado):")
for prato in pratos:
    print("- " + prato.title())

print("\nTupla (revisado): " + str(pratos))
