import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import itertools


def convert_list(org_list):
	return([np.nan if i == '' else float(i) for i in org_list])

i, j = 1, 365
temp_dates, max_temps, min_temps, mean_temps = [], [], [], []

with open('RequestData/2temp-torontocc-daily-01012010-12312010.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for col1, col2, col3, col4 in itertools.islice(spamreader, i, j+1):
		temp_dates.append(col1[5:])
		max_temps.append(col2)
		min_temps.append(col3)
		mean_temps.append(col4)

max_temps = convert_list(max_temps)
min_temps = convert_list(min_temps)
mean_temps = convert_list(mean_temps)
x = np.arange(1,366)


dates = []

with open('RequestData/AllRequests.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "Pot Hole" in reason:
			dates.append(date[0:10])

day_month = [dates[i][0:5] for i in range(len(dates))]

c = Counter(day_month)
days, count = zip(*sorted(c.items()))

temp3 = [item for item in temp_dates if item not in list(days)]

new_list = zip(list(days) + temp3, list(count) + [0]*len(temp3))


days2, count2 = zip(*sorted(list(new_list)))


A = pd.Series(count2[0:50])
B = pd.Series(min_temps[0:50])

d = {'one': A, 
	 'two': B}

df = pd.DataFrame(d)

ax = df.one.plot(kind='bar')
ax = df.two.plot(secondary_y=True,color='r')



plt.show()
