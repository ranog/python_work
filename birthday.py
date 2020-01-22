#!/usr/bin/env python3
# O programa deseja feliz aniversário a alguém.

age = 23

# Essa linha gera um - TypeError: must be str, not int
# message = "Happy " + age + "rd Birthday!"

# Para representar valores que não são strings como strings:
message = "Happy " + str(age) + "rd Birthday!"

print(message)
