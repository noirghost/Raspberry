#!/bin/bash

# Download CEST time from python script
user=$(whoami)
time=$(python3 /home/$user/Soft/time/rpi_time-converter.py)

# Set date from google server
curl -I --silent https://google.com | grep date > /tmp/date.txt

date_day=$(cat /tmp/date.txt | awk '{print $3}')
date_month=$(cat /tmp/date.txt | awk '{print $4}')
date=$(echo $date_day'+'$date_month)

# Setting actual date
sudo  date --set $date
clear

# Setting actual time
sudo timedatectl set-time $time
