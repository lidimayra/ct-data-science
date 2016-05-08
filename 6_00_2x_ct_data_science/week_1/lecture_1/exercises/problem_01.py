# -*- coding: utf-8 -*-
"""
Created on Sun May 01 22:40:04 2016

@author: Lidiane
"""

def isAlphabeticalWord(word, wordList=None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList

wordList = ['box', 'annoy', 'bat' , 'chips']
print(isAlphabeticalWord('box', wordList))
print(isAlphabeticalWord('bat', wordList))
print(isAlphabeticalWord('abc', wordList))

print(isAlphabeticalWord('bat'))