import csv
import itertools
import numpy as np
import matplotlib.pyplot as plt
import calendar

def convert_list(org_list):
	return([np.nan if i == '' else float(i) for i in org_list])

i, j = 1, 365
dates, max_temps, min_temps, mean_temps = [], [], [], []

with open('RequestData/2temp-torontocc-daily-01012010-12312010.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for col1, col2, col3, col4 in itertools.islice(spamreader, i, j+1):
		dates.append(col1)
		max_temps.append(col2)
		min_temps.append(col3)
		mean_temps.append(col4)

max_temps = convert_list(max_temps)
min_temps = convert_list(min_temps)
mean_temps = convert_list(mean_temps)
x = np.arange(1,366)

plt.plot(x, max_temps, x, min_temps, x, mean_temps)
# plt.xticks(np.arange(12), calendar.month_name[1:13], rotation=17)
plt.show()