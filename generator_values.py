from datetime import datetime, timedelta
import csv
import logging
import random
import sys

logging.basicConfig(filename='data.log', level=logging.DEBUG)

_author_ = 'Maurizio Bussi'

# static variable
MIN_VALUE = 3.0
MAX_VALUE = 6.0
THRES_TOLL = 0.5
AVAILABLE_OPTIONS = [
	round(random.uniform(MIN_VALUE, MAX_VALUE), 1),
	round(random.uniform(MIN_VALUE, MIN_VALUE - THRES_TOLL), 1),
	round(random.uniform(MAX_VALUE, MAX_VALUE + THRES_TOLL), 1),
	round(random.uniform(0.0, MIN_VALUE - THRES_TOLL - 0.1), 1),
	round(random.uniform(MAX_VALUE + THRES_TOLL + 0.1, 8.0), 1),
	'null'
]
# print AVAILABLE_OPTIONS[1]

 

dates_to_check = ['20/11/2017', '21/11/2017', '22/11/2017']

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%H:%M') for dt in 
       datetime_range(datetime(2017, 11, 20, 0), datetime(2017, 11, 21, 0), 
       timedelta(minutes=15))]

def write_on_file():
	logging.info('start writing the file')
	with open('values.csv', 'ab') as f:
		logging.info('write value per date')
   		fieldnames = ['DATA', 'ORA', 'POM_ID', 'DEVICE_ID', 'VALUE'] 
    		writer = csv.DictWriter(f, fieldnames=fieldnames)

		for dt in dates_to_check:
			for i in range(0, 96):
				writer.writerow({
					'DATA': dt,
					'ORA': dts[i],
					'POM_ID': sys.argv[1],
					'DEVICE_ID': sys.argv[1],
					'VALUE': AVAILABLE_OPTIONS[random.randint(0, len(AVAILABLE_OPTIONS) - 1)],
				})


def start():
	write_on_file()
	logging.info("file generated successfully!!\n-------------------------------")


start()

