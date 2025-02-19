# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:57:37 2020

@author: israe
"""

from collections import  Counter
import matplotlib.pyplot as plt


num_friends = [100, 49, 41, 40 ,25]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")