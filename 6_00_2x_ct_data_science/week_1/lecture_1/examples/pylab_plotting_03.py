# -*- coding: utf-8 -*-
"""
Created on Mon May 02 00:51:02 2016

@author: Lidiane
"""

import pylab

principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years + 1), values, 'r-', linewidth = 30)
pylab.title('5% Growth, Compounded Annually', fontsize = 12)
pylab.xlabel('Years of Compounding', fontsize = 6)
pylab.ylabel('Value of Principal ($)', fontsize = 20)
pylab.show()