import os
import sys
import csv
import random 

def force_value(mylist, new_value):
  for i in range(0, 33):
    mylist[random.randint(0, len(mylist) - 1)] = float(new_value)

def read_file():
  with open('values.csv') as f:
    reader = csv.DictReader(f)
    values = [row['VALUE'] for row in reader]
    force_value(values, sys.argv[1])
 
    return values

print read_file()
