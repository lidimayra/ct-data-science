# -*- coding: utf-8 -*-
"""
Created on Mon May 02 01:46:17 2016

@author: Lidiane
"""

import pylab

def loadTemps():
    inFile = open('julyTemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return(low, high)    

def diffTemps():
    low = loadTemps()[0]
    high = loadTemps()[1]
    temps = zip(high, low)
    diff = []
    for h, l in temps:
        diff.append(h-l)
    return diff

diff = diffTemps()    
pylab.plot(range(1, len(diff)+1), diff)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()