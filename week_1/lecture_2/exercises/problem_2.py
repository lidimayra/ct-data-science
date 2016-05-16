# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:13:55 2016

@author: Lidiane
"""

import random

def genEven():
    numbers = []
    for i in range(100):
        if i%2 == 0:
            numbers.append(i)
    number = random.choice(numbers)
    return number

def genEven2():
    return random.randrange(0, 100, 2)

print (genEven())
print (genEven2())