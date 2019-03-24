import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import matplotlib as mpl
import numpy as np
from pylab import rcParams

from Financemanager.graph import value_manager

"""Give, how much you made each day, and it draws the graph
     y_money = int of how much you made each day
     x_date = the date you made the money"""

def draw_graph(y_money, x_date, goal=[]):



    counter = -1
    now_money = []

    plt.figure(1)
    for value in y_money:

        if counter >= 0:
            before_value = now_money[-1]
            now_value = before_value + y_money[counter+1]
            now_money.append(now_value)
            counter += 1

        else:
            now_money.append(y_money[0])
            counter += 1
    mpl.rcParams['toolbar'] = 'None'
    plt.plot(now_money, "blue", label="Money")

    #mpl.rcParams['figure.figsize'] = 8, 12

    before = 0
    counter_2 = 0

    #  Show if before value was lower than now value(red/green)
    for element in now_money:

        if element >= int(before):
            plt.scatter(x_date[counter_2], element, c="green", s=50)
            counter_2 += 1
            before = element

        else:
            plt.scatter(x_date[counter_2], element, c="red", s=50)
            counter_2 += 1
            before = element

    x_tick = []
    for item in x_date:
        try:
            x_tick.append(item[:3])
        except IndexError:
            x_tick.append("")


    plt.xticks(np.arange(7), x_tick)

    # 0 graph
    mpl.rcParams['toolbar'] = 'None'

    zero_lenght = []
    for value in x_date:
        zero_lenght.append(0)

    plt.plot(x_date, zero_lenght, "black", linewidth=2)

    # Goal graph
    mpl.rcParams['toolbar'] = 'None'

    for g in goal:
        y_values = []

        for value in x_date:
            y_values.append(int(g[1]))
        plt.plot(x_date, y_values, label=g[0], linewidth=1.5, linestyle='--')
        plt.legend()
    plt.legend()
    plt.show()


#draw_graph(value_manager.get_value_week()[1], value_manager.get_value_week()[0], value_manager.goal_values_all())



