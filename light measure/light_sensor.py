#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def sensor(pin):
    global count
    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == GPIO.LOW:
        count += 1


while True:
    sensor(21)
    filter = int(count + int(count/2)) 
#    print('filter = ', filter)

    for x in range(15):
        file = open('/home/pi/Soft/light/database.txt', 'a')
        sensor(21)
        percent = int(count / filter)
        file.write(str(percent) + '\n')
        file.close() 
        print(percent)
        time.sleep(0.7)
