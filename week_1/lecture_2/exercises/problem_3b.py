# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:44:09 2016

@author: Lidiane
"""

import random

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even
    number between 9 and 21
    '''    
    return random.randrange(10, 22, 2)
    
print (stochasticNumber())
