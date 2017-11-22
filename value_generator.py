import csv
import datetime
import logging
import random


# static variable
MIN_VALUE = 3
MAX_VALUE = 6
THRES_TOLL = 0.5 

def write_on_file():
  with open('values.csv', 'ab') as f:
    fieldnames = ['DATA', 'ORA', 'POM_ID', 'DEVICE_ID', 'VALUE'] 
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writerow({
      'DATA':'20/11/2017',
      'ORA':'00:00',
      'POM_ID': 1,
      'DEVICE_ID': 1,
      'VALUE': 3
    })


def start():
  write_on_file()


start()      
