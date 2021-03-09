import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos:
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15) 

# Salva o gráfico automaticamente:      
plt.savefig('random_walk_plot.png')

plt.show()
