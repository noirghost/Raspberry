#!/usr/bin/python3

#!/usr/bin/python3
from datetime import date
import os

year = int(os.popen("curl -I --silent https://google.com | grep date | awk '{print $5}'").read().strip('\n'))
month = os.popen("curl -I --silent https://google.com | grep date | awk '{print $4}'").read().strip('\n')
day = int(os.popen("curl -I --silent https://google.com | grep date | awk '{print $3}'").read().strip('\n'))

conv_month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
             }

winter_months = [11, 12, 1, 2]
summer_months = [4, 5, 6, 7, 8, 9]
center_months = [10, 3]

def summer_time(): 
    GMT_time = os.popen("curl -I --silent https://google.com | grep date | awk '{print $6}'").read().strip('\n')
    mod_time = GMT_time.split(':')

    if int(mod_time[0] == 22):
        mod_time[0] = '00'
    elif int(mod_time[0]) == 23:
        mod_time[0] = '00'
        mod_time[0] = str(int(mod_time[0]) + 1) 
    else:
        mod_time[0] = str(int(mod_time[0]) + 2) 
    
    CEST_time = ':'.join(mod_time)
    print(CEST_time)
    
    
def winter_time():
    GMT_time = os.popen("curl -I --silent https://google.com | grep date | awk '{print $6}'").read().strip('\n')
    mod_time = GMT_time.split(':')

    if int(mod_time[0] == 23):
        mod_time[0] = '00'
    else:
        mod_time[0] = str(int(mod_time[0]) + 1) 
    
    CEST_time = ':'.join(mod_time)
    print(CEST_time)    


def october():
    last = []
    
    if conv_month[month] == 10:
        for x in range(day, 32):
            day_numb = date(year, conv_month[month], x).weekday()
            last.append(day_numb)
        del last[0]
        if 6 in last:
            summer_time()
        else:
            winter_time()


def march():
    last = []    
    
    if conv_month[month] == 3:
        for x in range(day, 31):
            day_numb = date(year, conv_month[month], x).weekday()
            last.append(day_numb)
        del last[0]
        if 6 in last:
            winter_time()
        else:
            summer_time()
 
     
if conv_month[month] in center_months:
    october()    
    march()

elif conv_month[month] in winter_months:
    winter_time()    

elif conv_month[month] in summer_months:
    summer_time()
