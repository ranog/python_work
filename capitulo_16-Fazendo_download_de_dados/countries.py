#!/usr/bin/env python3

from pygal.maps.world import COUNTRIES

# coloca as chaves em ordem alfabéfica.
for country_code in sorted(COUNTRIES.keys()):
    # exibe o código de cada país e o nome associado. 
    print(country_code, COUNTRIES[country_code])
