import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import calendar
import datetime
import operator

dates = []
reasons = []

white_goods = []
water_service = []
sewer_service = []
residential_furniture = []
res_garbage = []
res_recycle = []
res_green = []


with open('SixtyFiveThousand.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for date, reason in spamreader:
		if "All / White Goods / Pick Up Request" in reason:
			white_goods.append(date[0:2])

		if "Water Service Line-Turn Off" in reason:
			water_service.append(date[0:2])

		if "Sewer Service Line - Blocked" in reason:
			sewer_service.append(date[0:2])

		if "Residential Furniture / Missed" in reason:
			residential_furniture.append(date[0:2])

		if "Res / Garbage / Missed" in reason:
			res_garbage.append(date[0:2])

		if "Res / Recycle / Missed" in reason:
			res_recycle.append(date[0:2])

		if "Res / Organic Green Bin / Missed" in reason:
			res_green.append(date[0:2])


counter_white_goods = Counter(white_goods)
months_white_goods, count_white_goods = zip(*sorted(counter_white_goods.items()))

counter_water_service = Counter(water_service)
months_water_service, count_water_service = zip(*sorted(counter_water_service.items()))

counter_sewer_service = Counter(sewer_service)
months_sewer_service, count_sewer_service = zip(*sorted(counter_sewer_service.items()))

# # # # # # PY PLOT 

# print(np.array(count_white_goods)+np.array(count_water_service), list(map(sum,zip(count_white_goods,count_water_service))), list(map(operator.add, count_white_goods,count_water_service)))

indexes = np.arange(len(months_white_goods))
width = 0.15


p1 = plt.bar(indexes, count_white_goods, width, color='r')
p2 = plt.bar(indexes, count_water_service, width, color='y', bottom=count_white_goods)
# # p3 = plt.bar(indexes, count_sewer_service, width, color='b', bottom=np.array(count_white_goods)+np.array(count_water_service))
p3 = plt.bar(indexes, count_sewer_service, width, color='b', bottom=list(map(operator.add, count_white_goods,count_water_service)))
plt.xticks(indexes+width/2., months_white_goods)

plt.show()

# # plt.bar(indexes, count, width, color='r')
# # plt.xticks(indexes + width * 0.2, m)
# # plt.show()

# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'white', 'red', 'red']
# explode = (0, 0, 0.1, 0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

# plt.pie(count, labels=m, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90, colors=colors)
# plt.axis('equal')

# plt.show()