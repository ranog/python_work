#!/usr/bin/env python3

# Exemplo de uma lista simples

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Acessando elementos de uma lista
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1]) 
print(bicycles[3])

# Acessar o último elemento de uma lista
print(bicycles[-1])
print(bicycles[-2])

# Usando valores individuais de uma lista
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
