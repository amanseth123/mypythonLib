import numpy as np
import matplotlib.pyplot as plt
import csv
def plot(sheetName):
    x = []
    y = []
    with open(sheetName,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0])) # time stamp
            y.append(int(row[1])) # average sales
    plt.plot(x,y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

