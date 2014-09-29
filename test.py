# from collections import Counter
# import numpy as np
# import matplotlib.pyplot as plt


# labels, values = zip(*Counter(['A','B','A','C','A','A']).items())

# print(values)

# # indexes = np.arange(len(labels))
# # width = 1

# # plt.bar(indexes, values, width)
# # plt.xticks(indexes + width * 0.5, labels)
# # plt.show()


# import numpy as np

# dataset = [12, 5, 6, 3, 1, 1]

# def movingaverage(values,window):
#     weigths = np.repeat(1.0, window)/window
#     smas = np.convolve(values, weigths, 'valid')
#     return smas

# #Will print out a 3MA for our dataset
# print(movingaverage(dataset,3))

import datetime

# today = datetime.datetime.now()
mydate = datetime.datetime.strptime('01-03','%m-%d').strftime('%B')

# day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

print(mydate)