import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
import collections

sample = np.random.choice(['a', 'b'], size=10)

# c = collections.Counter(sample)

s = Series(sample)

vc = s.value_counts()
vc = vc.sort_index()

print(vc)

# vc.plot(kind='bar')
# plt.show()

# print(s)