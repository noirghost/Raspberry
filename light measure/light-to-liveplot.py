#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time 


count2 = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def analog(pin):
    file = open('/home/pi/tmp/database.txt', 'a')
    count = 0
    global count2
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.9)
    
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    
    percent = int(count / 80)
    count2 += 50
     
    plt.axis([0, 5000, 0, 300])
    plt.scatter(count2, percent)
    plt.grid(True)
    plt.pause(0.05)
    
    file.write(str(percent) + '\n')
    file.close()
    return percent
    
while True:
    print(analog(4))
    
plt.show()    
