#! /usr/bin/env python3

"""
NOME
    todas_funcoes_310.py

SINOPSES
    chmod +x todas_funcoes_310.py
    ./todas_funcoes_310.py

DESCRIÇÃO
    3.10 - Todas as funções: Pensa em algo que você poderia armazenar em uma
    lista. Por exemplo, voçê poderia criar uma lista de montanhas, rios,
    países, cidades, idiomas ou qualquer outro item que quiser. Escreva um
    programa que crie uma lista contendo esses itens e então utilize cada
    função apresentada neste capítulo pelo menos uma vez.

----------------------------------------------------------------------

HISTÓRICO
    20201903: João Paulo, março de 2020.
        Rascunho do cabeçalho do execício 3.10 da página 83, Capítulo 3 -
        Introdução às listas

    20201210: João Paulo, outubro de 2020.
        Milésima tentativa de retornar a estudar python.
        Site da minha lista de cidades: https://mestre-cervejeiro.com/roteiro-de-viagem-cervejeira-para-a-belgica/

"""

cidades = ['bruxelas', 'mechelen', 'puurs', 'antuérpia', 'tilburg', 'bruges',
'vleteren']

print(cidades)                  # lista
print(cidades[0])               # devolver o 1° elemento da lista
print(cidades[0].title())       # começar com letra maiúscula
print(cidades[1])               # devolver 2° elemento da lista
print(cidades[3])               # devolver 4° elemento da lista
print(cidades[-1])              # devolver último elemento da lista

mensagem = "\nViagem Cervejeira pela Bélgica: Roteiro completo (9 dias)\n- Dia\
1: Chegada em " + cidades[0].title() + "."

print(mensagem)                 # mensagem concatenada

cervejarias = ['krios', 'carijó', 'villa puri', 'araukarien',
'pinhalense', 'ikaros']

print()
print(cervejarias)      # lista original

cervejarias[0] = 'los dias'
print(cervejarias)      # lista alterada

cervejarias.append('browe') # concatenar

print(cervejarias)

cervejarias.insert(0, 'fritz') # inserir
print(cervejarias)

del cervejarias[1]  # del- usar quando a posição do item for conhecida (não da para usar o elementos após o uso do del)
print(cervejarias)

popped_cervejarias = cervejarias.pop()  # pop - dá para usar o item após removè-lo
print(cervejarias)
print(popped_cervejarias)

""" Quando quiser apagar um item de uma lista e esse item não vai ser usado de modo algum, utilize a
instrução del ; se quiser usar um item à medida que removê-lo, utilize o método pop() .
"""

cervejarias.remove('araukarien')   # remove() - usar quando conhecer apenas o valor do item
print(cervejarias)

nao_vale = 'fritz'
cervejarias.remove(nao_vale)
print(cervejarias)
print("\nO " + nao_vale.title() + " não é uma cervejaria do Vale do Paraíba.")

""" O método remove() apaga apenas a primeira ocorrência do valor que você especificar.
Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário
usar um laço para determinar se todas as ocorrências desse valor foram removidas.
"""

print("\n- Ordenando uma lista de forma permanente com o método sort():")
cervejarias.sort()
print(cervejarias)

cervejarias.sort(reverse=True)
print(cervejarias)

print("\n- Ordenando uma lista temporariamente com a função sorted()")
print(sorted(cervejarias))
print(cervejarias)

print("\n- Exibindo uma lista em ordem inversa")
cervejarias.reverse()
print(cervejarias)

""" O método reverse() muda a ordem de uma lista de forma permanente,
mas podemos restaurar a ordem original a qualquer momento aplicando
reverse() à mesma lista uma segunda vez.
"""

print("\n- Descobrindo o tamanho de uma lista - len()")
print(cervejarias)
print(len(cervejarias))

""" Python conta os itens de uma lista começando em um, portanto você
não deverá se deparar com nenhum erro de deslocamento de um ao
determinar o tamanho de uma lista.
"""
