import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from machine_learning.utils.database_loader import load_database

def plot (file_name, classe_a = '0', classe_b = '1', separator = ','):
    database = load_database(file_name, separator)
    x_a = [v[0] for v in filter(lambda e: e[-1] == classe_a, database)]
    y_a = [v[1] for v in filter(lambda e: e[-1] == classe_a, database)]
    x_b = [v[0] for v in filter(lambda e: e[-1] == classe_b, database)]
    y_b = [v[1] for v in filter(lambda e: e[-1] == classe_b, database)]
    
    plt.plot(x_a, y_a, 'r--', x_b, y_b, 'bs')
    plt.show()



def old_plot():    
    #configurando propriedades
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #Carregando Bases

    banana_a_x, banana_a_y = carregar_base('b_a.txt')
    banana_b_x, banana_b_y = carregar_base('b_b.txt')

    #Passar como parametro as  caracteristicas
    ax.plot(banana_a_x, banana_a_y, 'rx', banana_b_x, banana_b_y, 'go')
    #ax.plot(banana_b_x, banana_b_y, 's')
    ax.set_title('Banana data set')
    plt.show()


if __name__ == '__main__':
    plot('artificial_databases/a_database.data')




