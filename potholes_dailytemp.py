import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from itertools import islice
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.dates as dates
import seaborn as sns

sns.set_style("dark", {"grid.linewidth": .5, "axes.facecolor": ".9",'xtick.major.size': 5})

## Read temperature data

def convert_list(org_list):
	# Puts NaN on days when a temperature wasn't recorded
	# and converts temperatures to float.
	return([np.nan if i == '' else float(i) for i in org_list])

## Read temperature data
dates_temps, max_temps, min_temps, mean_temps = [], [], [], []

with open('RequestData/2temp-torontocc-daily-01012010-12312010.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for col1, col2, col3, col4 in islice(spamreader, 1, 366):
		dates_temps.append(col1[5:])
		max_temps.append(col2)
		min_temps.append(col3)
		mean_temps.append(col4)

max_temps = convert_list(max_temps)
min_temps = convert_list(min_temps)
mean_temps = convert_list(mean_temps)


## Read 311 data
request_dates = []

with open('RequestData/AllRequests.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "Pot Hole" in reason:
			request_dates.append(date[0:10])

request_months = [request_dates[i][0:5] for i in range(len(request_dates))]

# Following line adds missing (days in which no requests were made) days to request_months
temp_list = (list(request_months) + [day for day in dates_temps if day not in list(request_months)])

c = Counter(temp_list)
request_days, request_count = zip(*sorted(c.items()))


## Plot request_days of week on X-axis

weekday_names = [datetime.datetime.strptime(i+'-2010', '%m-%d-%Y').strftime('%a') for i in request_days]

i = 10 # 
j = 80 # 

idx = [datetime.datetime(2010, 1, 1) + datetime.timedelta(days=x) for x in range(i, j)]

A = pd.Series(request_count[i:j], index=weekday_names[i:j])
B = pd.Series(min_temps[i:j], index=weekday_names[i:j])

fig, ax1 = plt.subplots()
ax1.bar(idx, A, align='center')
ax1.set_ylabel("Number Of Complaints")
ax1.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=(0,4),interval=1))
ax1.xaxis.set_major_formatter(dates.DateFormatter('%d\n%b\n%a'))
ax1.xaxis.grid(True, which="major")
ax1.xaxis.set_ticks_position('bottom')

ax2 = ax1.twinx()
ax2.plot(idx, B, color='r')
ax2.set_ylabel('Mean Daily Temp. (deg C)')
 
plt.tight_layout()
plt.show()



########################

'''
idx = pd.date_range('2010-01-01', '2010-03-20')
A = pd.Series(request_count[0:79], index=idx)
B = pd.Series(min_temps[0:79], index=idx)

d = {'one': A, 'two': B}
df = pd.DataFrame(d)

fig, ax1 = plt.subplots()
ax1.plot_date(idx.to_pydatetime(), A, '-')
ax1.plot

ax2 = ax1.twinx()
ax2.plot_date(idx.to_pydatetime(), B, '-', color='r')

ax1.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=(0),interval=1))
ax1.xaxis.set_major_formatter(dates.DateFormatter('%d\n%a'))
ax1.xaxis.grid(True, which="major")
ax1.yaxis.grid()
ax1.set_ylabel('311 Calls')

ax2.set_ylabel('Temp')

plt.legend() 
plt.show()
'''