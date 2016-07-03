# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:16:21 2016

@author: Chang
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fig = plt.figure(figsize=(6,6))
#fig, ax = plt.subplots(figsize=(6,6))
x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9])
plt.boxplot(x)
plt.xlabel('Sample')
plt.axis([0,2,0,10])
plt.show()


fig =plt.figure(figsize=(6,6))
plt.hist(x,bins=10,normed=True)
plt.xlabel('Numbers')
plt.ylabel('Probability')
plt.show()

fig = plt.figure(figsize=(6,6))
pp = stats.probplot(x,dist='norm',plot=plt)
plt.xlabel('theoretical quantile')
plt.ylabel('sample values')
plt.show()



