import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
import datetime


dates = []

# with open('AllRequests.csv', 'r') as csvfile:
with open('RequestData/SixtyFiveThousand.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "Pot Hole" in reason:
			dates.append(date[0:10])


day_month = [dates[i][0:2] for i in range(len(dates))]

c = Counter(day_month)
months, count = zip(*sorted(c.items()))

word_month = []
for month in months:
	word_month.append(datetime.datetime.strptime(month,'%m').strftime('%B'))

word_day = []
for day in dates:
	word_day.append(datetime.datetime.strptime(day,'%m-%d-%Y').strftime('%A'))




# # PY PLOT 


indexes = np.arange(len(months))
width = 1

plt.bar(indexes, count, width, color='r')
plt.xticks(indexes + width * 0.5, word_month)
plt.show()



# # USING PANDAS

# s = Series(dates)
# vc = s.value_counts()
# vc = vc.sort_index()

# vc.plot(kind='bar')
# plt.show()
