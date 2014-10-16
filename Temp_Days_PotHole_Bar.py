import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from itertools import islice
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.dates as dates


## Read temperature data

def convert_list(org_list):
	# Gets rid of blank days in temp data, replaces with NaN
	return([np.nan if i == '' else float(i) for i in org_list])

i, j = 1, 365
temp_dates, max_temps, min_temps, mean_temps = [], [], [], []

with open('RequestData/2temp-torontocc-daily-01012010-12312010.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for col1, col2, col3, col4 in islice(spamreader, i, j+1):
		temp_dates.append(col1[5:])
		max_temps.append(col2)
		min_temps.append(col3)
		mean_temps.append(col4)

max_temps = convert_list(max_temps)
min_temps = convert_list(min_temps)
mean_temps = convert_list(mean_temps)
x = np.arange(1,366)

## Read 311 data

request_date = []

with open('RequestData/AllRequests.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "Pot Hole" in reason:
			request_date.append(date[0:10])

day_month = [request_date[i][0:5] for i in range(len(request_date))]

c = Counter(day_month)
days, count = zip(*sorted(c.items()))

# Fill in days where no 311 requests were made

temp_list = [item for item in temp_dates if item not in list(days)]
new_list = zip(list(days) + temp_list, list(count) + [0]*len(temp_list))

days2, count2 = zip(*sorted(list(new_list)))

# Plot days of week on X-axis
'''
dates_weekday = [datetime.datetime.strptime(i+'-2010', '%m-%d-%Y').strftime('%a') for i in days2]

A = pd.Series(count2[0:79], index=dates_weekday[0:79])
B = pd.Series(min_temps[0:79], index=dates_weekday[0:79])
d = {'one': A, 'two': B}
df = pd.DataFrame(d)

ax = df.one.plot(kind='bar')
ax = df.two.plot(secondary_y=True,color='r')

ax.left_ax.set_ylabel("Number Of Complaints")
ax.right_ax.set_ylabel('Mean Temp. (deg C)')

# plt.gcf().autofmt_xdate() 
plt.show() 
'''


idx = pd.date_range('2010-01-01', '2010-03-20')
A = pd.Series(count2[0:79], index=idx)
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
plt.tight_layout()
plt.show()


