#!/usr/bin/python3
import os
from bottle import route, run, template

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return cpu_temp


@route('/temp')
def temp():
    return cpu_temp() 

@route('/')
def index():
    return template('index.html')

run(host='localhost', port=8080, debug=True, reloader=True)


