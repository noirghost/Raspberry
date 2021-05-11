#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import os

plt.ion()

while True:
    file = open('/home/ghost/Soft/light-client/database.txt')
    y = np.loadtxt(file)
    count = len(y)
    x = np.arange(count)
    plt.plot(x,y)
    plt.draw()
    plt.pause(30)
    plt.clf()
    os.system('scp -P 2222 pi@192.168.1.25:/home/pi/Soft/light/database.txt /home/ghost/Soft/light-client')

