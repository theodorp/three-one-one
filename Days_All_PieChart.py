## Plots all requests in a pie chart divided by the days of the week the request was made

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import calendar
import datetime
import seaborn as sns

dates = []

with open('RequestData/AllRequests.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		# if "Road" in reason:
		dates.append(date[0:10])

word_day = []
for day in dates:
	# word_day.append(datetime.datetime.strptime(day,'%m-%d-%Y').strftime('%A'))
	word_day.append(datetime.datetime.strptime(day,'%m-%d-%Y').weekday())


m = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

weekday_tuples = list(Counter(word_day).items())

day, count = zip(*weekday_tuples)

# # # # PY PLOT 

indexes = np.arange(len(day))
width = 1

plt.bar(indexes, count, width)
plt.xticks(indexes + width * 0.5, m)
plt.show()

# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'white', 'red', 'blue']
# explode = (0, 0, 0.1, 0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

# plt.pie(count, labels=m, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90, colors=colors)
# plt.axis('equal')

# plt.show()