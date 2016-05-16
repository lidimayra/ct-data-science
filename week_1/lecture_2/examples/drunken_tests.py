# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:05:32 2016

@author: Lidiane
"""

from drunken_walks import Location, Field, UsualDrunk

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials = 20):
    # import random
    # random.seed(0)    
    
    #for numSteps in [0, 1]:
    for numSteps in [10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print 'Mean = ', sum(distances)/len(distances)
        print 'Max = ', max(distances), 'Min =', min(distances)
        
print drunkTest()
    