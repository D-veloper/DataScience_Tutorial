import pandas as pd
import matplotlib.pyplot as plt

# series pd.Series([values], [keys])
series = pd.Series(['A', 'B', 'C', 'D'], [10, 20, 30, 40])

# print(series[10])
# print(series.iloc[0]) both return A. Access series by keys or index location.

series.name = "test"  # give a series a name.

# print(dict(series))  # easily convert dictionary to series.

s1 = pd.Series([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
s2 = pd.Series([4, 3, 2, 1], ['B', 'D', 'A', 'C'])

# print(s1 + s2)  # you can add series together, granted they have the same keys.
# print(s1.count())  # get the length of a series.
# print(s1.head())  # print the first 5 rows by default or specify
# print(s1.tail(2))  # print the last 2 rows

def square(x):
    return x ** 2
#
# print(s2.apply(square))  # apply functions on all elements in a series.

# print(s2.sort_index())  # sort by keys
# print(s2.sort_values())  # sort by values
s2.sort_values(inplace=True)  # instead of returning a sorted copy, this sorts the actual series

s3 = s1 + s2
s3 = s3.apply(square)

s3.plot.bar()
plt.ylim(5, 50)
plt.show()
