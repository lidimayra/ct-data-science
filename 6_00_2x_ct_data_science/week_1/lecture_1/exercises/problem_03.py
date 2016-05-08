# -*- coding: utf-8 -*-
"""
Created on Mon May 02 01:46:17 2016

@author: Lidiane
"""

def loadTemps():
    inFile = open('julyTemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(fields[1])
            low.append(fields[2])
    return(low, high)    
 
print loadTemps()