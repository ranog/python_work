#!/usr/bin/env python3

import json

# Carrega os dados em uma lista:
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Exibe a população de cada país em 2010:
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        print(country_name + ": " + str(population))
