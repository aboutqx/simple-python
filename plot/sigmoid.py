#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.arange(-4, 4, 0.2)
    y = 1/(1 + np.exp(-x))
    plt.figure(1)

    plt.subplot(221)
    plt.plot(x, y)
    plt.title('sigmoid')

    plt.subplot(222)
    x = np.arange(-60, 60, 0.2)
    y = 1/(1 + np.exp(-x))
    plt.plot(x, y)
    plt.title('sigmoid like step')

    plt.subplot(223)
    plt.plot(x, x*2)
    plt.title('linear')

    plt.show()

main()

