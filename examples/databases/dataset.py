import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def carregar_base(arquivo):
	input = open(arquivo, 'r')
	elementos = []
	eixo_x = []
	eixo_y = []
	a = input.readline()
	while a:
		elementos.append(a.split(','))	
		a = input.readline()
	
	for e in elementos:
		eixo_x.append(e[0])
		eixo_y.append(e[1])
	
	input.close()
	
	return eixo_x, eixo_y
	
#configurando propriedades
matplotlib.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = fig.add_subplot(111)

#Carregando Bases

banana_a_x, banana_a_y = carregar_base('banana_a.txt')
banana_b_x, banana_b_y = carregar_base('banana_b.txt')

#Passar como parametro as  caracteristicas
ax.plot(banana_a_x, banana_a_y, 'rx', banana_b_x, banana_b_y, 'go')
#ax.plot(banana_b_x, banana_b_y, 's')
ax.set_title('Banana data set')
plt.show()
