import numpy as np
import matplotlib.pyplot as plt


def plot_dataset(dataset, title = None, colors = None):
    ax = get_ax()
    

    classes = set([data[-1] for data in dataset])
    for i in range(len(classes)):
        c = classes[i]
        dataset_c = filter(lambda data: data[-1] == c, dataset)
        eixo_x = [data[0] for data in dataset_c]
        eixo_y = [data[1] for data in dataset_c]
        ax.plot(eixo_x, eixo_y, colors[i])
        
    ax.set_title(title)
    ptl.show()



def get_ax():
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    return ax

