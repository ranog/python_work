#!/usr/bin/env python3

import pygal
from die import Die


# Cria dois dados D8:
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista:
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analisa os resultados:
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados:
hist = pygal.Bar()
hist.title = "Results of rolling three D6 1000 times."
hist.x_labels = [str(x_label) for x_label in range(3,19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('tres_dados_visual.svg')
