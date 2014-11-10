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

sns.set_style('dark', {"grid.linewidth": .5, "axes.facecolor": "white", 
						'xtick.major.size': 5, 'grid.color': '.8', 
						'axes.edgecolor': '.8', 'legend.frameon': True})

# Puts NaN on days when a temperature wasn't recorded
# and converts temperatures to float.
def convert_list(org_list):
	return([np.nan if i == '' else float(i) for i in org_list])

## Read temperature data
data_temperature_dates, data_temperature_meantemp = [], []

with open('RequestData/2temp-torontocc-daily-01012010-12312010.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for col1, col2, col3, col4 in islice(spamreader, 1, 366):
		data_temperature_dates.append(col1[3:8])
		data_temperature_meantemp.append(col4)

data_temperature_meantemp = convert_list(data_temperature_meantemp)


## Read 311 data
data_311_dates = []

with open('RequestData/AllRequests.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "Pot Hole" in reason:
			data_311_dates.append(date[0:10])

data_311_dates_months = [data_311_dates[i][0:5] for i in range(len(data_311_dates))]

# Following line adds missing (days in which no requests were made) days to data_311_dates_months

# Generates list of days for 2010, and formats them into %m-%d
datelist = [datetime.datetime(2010, 1, 1) + datetime.timedelta(days=x) for x in range(0,365)]
datelist_formatted = [datelist[i].strftime("%m-%d") for i in range(len(datelist))]

# Compares list of days from data with full year and adds the days that are missing
temp_list = (list(data_311_dates_months) + [day for day in datelist_formatted if day not in list(data_311_dates_months)])
data_temperature_dates = (list(data_temperature_dates) + [day for day in datelist_formatted if day not in list(data_temperature_dates)])


## Count number of times a complaint occured on a given day
c = Counter(temp_list)
complaint_day, complaint_counter = zip(*sorted(c.items()))


## Plot complaint_day of week on X-axis

weekday_names = [datetime.datetime.strptime(k+'-2010', '%m-%d-%Y').strftime('%a') for k in complaint_day]

i = 0 # 
j = 172 # 
# j = 364

idx = [datetime.datetime(2010, 1, 1) + datetime.timedelta(days=x) for x in range(i, j)]

A = pd.Series(complaint_counter[i:j], index=weekday_names[i:j])
B = pd.Series(data_temperature_meantemp[i:j], index=weekday_names[i:j])

fig, ax1 = plt.subplots()
lns1 = ax1.bar(idx, A, align='center', color='b', edgecolor = "none", label="Number of Pothole Complaints")
ax1.set_ylabel("Number of Complaints")
ax1.set_title("Toronto 311 Pothole Complaints compared to Mean Daily Temperature")
ax1.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=(0),interval=1))
ax1.xaxis.set_major_formatter(dates.DateFormatter('%d\n%b\n'))
ax1.xaxis.grid(True, which="major")
ax1.xaxis.set_ticks_position('bottom')

ax2 = ax1.twinx()
lns2 = ax2.plot(idx, B, color='r', label="Mean Daily Temperature")
ax2.set_ylabel('Temp. (deg C)')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax2.legend(h1+h2, l1+l2, loc=0, fancybox=True, shadow=True)

fig.set_tight_layout(True)
plt.show()
fig.savefig('foo.pdf')



# ########################

# '''
# idx = pd.date_range('2010-01-01', '2010-03-20')
# A = pd.Series(complaint_counter[0:79], index=idx)
# B = pd.Series(min_temps[0:79], index=idx)

# d = {'one': A, 'two': B}
# df = pd.DataFrame(d)

# fig, ax1 = plt.subplots()
# ax1.plot_date(idx.to_pydatetime(), A, '-')
# ax1.plot

# ax2 = ax1.twinx()
# ax2.plot_date(idx.to_pydatetime(), B, '-', color='r')

# ax1.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=(0),interval=1))
# ax1.xaxis.set_major_formatter(dates.DateFormatter('%d\n%a'))
# ax1.xaxis.grid(True, which="major")
# ax1.yaxis.grid()
# ax1.set_ylabel('311 Calls')

# ax2.set_ylabel('Temp')

# plt.legend() 
# plt.show()
# '''