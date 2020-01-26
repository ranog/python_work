# - Pag. 75: Inserindo elementos em uma lista

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.insert(0, "ducati")
print(motorcycles)

# - Pag. 76: Removento elementos de uma lista

# Usando a instrução del
del motorcycles[0]
print(motorcycles)

# - Pag. 76-77: Removendo um item com o método pop()

# O método pop() remove o último item de uma lista, mas permite que
# trabalhe com esse item depois da remoção.

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# - Pag. 77-78: Removendo itens de qualquer posição em uma lista

motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + ".")

# Quando quiser apagar um item de uma lista e esse item não vai ser 
# usado de modo algum, utilize a instrução del; se quiser usar um 
# item à medida que removê-lo, utilize o metodo pop()

# - Pag. 78-79: Removendo um item de acordo com o valor
