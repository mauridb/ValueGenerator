import csv
import datetime
import logging
import random

logging.basicConfig(filename='data.log', level=logging.DEBUG)

# static variable
MIN_VALUE = 3.0
MAX_VALUE = 6.0
THRES_TOLL = 0.5
AVAILABLE_OPTIONS = [
	round(random.uniform(MIN_VALUE, MAX_VALUE), 1),
	round(random.uniform(MIN_VALUE, MIN_VALUE - THRES_TOLL), 1),
	round(random.uniform(MAX_VALUE, MAX_VALUE + THRES_TOLL), 1),
	'null'
]
# print AVAILABLE_OPTIONS[1]

 

dates_to_check = ['20/11/2017', '21/11/2017', '22/11/2017']

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
					'ORA': 'ancora da sistemare',
					'POM_ID': 'da sistemare' ,
					'DEVICE_ID': 'da sistemare',
					'VALUE': AVAILABLE_OPTIONS[random.randint(0, len(AVAILABLE_OPTIONS) - 1)],
				})


def start():
	write_on_file()
	logging.info("file generated successfully!!\n-------------------------------")


start()      
