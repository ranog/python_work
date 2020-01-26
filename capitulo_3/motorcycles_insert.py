print("# - Pag. 75: Inserindo elementos em uma lista:")

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.insert(0, "ducati")
print(motorcycles)


print("\n# - Pag. 76: Removento elementos de uma lista:")

# Usando a instrução del
del motorcycles[0]
print(motorcycles)


print("\n# - Pag. 76-77: Removendo um item com o método pop():")

# O método pop() remove o último item de uma lista, mas permite que
# trabalhe com esse item depois da remoção.

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)


print("\n# - Pag. 77-78: Removendo itens de qualquer posição em uma lista:")
# Modificando elementos de uma lista

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + ".")
print(motorcycles)

# Quando quiser apagar um item de uma lista e esse item não vai ser 
# usado de modo algum, utilize a instrução del; se quiser usar um 
# item à medida que removê-lo, utilize o metodo pop()

print("\n# - Pag. 78-79: Removendo um item de acordo com o valor:")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

# Também podemos usar o método remove() para trabalhar com um valor 
# que está sendo removido de uma lista

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
too_expensive = "ducati"

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# O método remove() apaga apenas a primeira ocorrência do valor. Se 
# o valor aparecer mais de uma vez na lista, será necessário usar um
# laço para determinar se todas as ocorrências desse valor foram 
# removidas.
