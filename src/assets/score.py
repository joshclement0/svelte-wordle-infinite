from audioop import reverse
import pandas as pd
import numpy as np

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

probs=[]
with open('limited1.txt','r') as f:
    lines = f.readlines()
    probs = [i[:-1].split(',') for i in lines]
cor = []
with open('limitedcor.txt','r') as f1:
    lines = f1.readlines()
    cor = [i[:-1].split(',') for i in lines]

def scoreCorrectWord(word):
    score = 0
    for i in range(5):
        w = word[i]
        score += float(probs[letters.index(w)][i+1])
        for j in range(4-i):
            k = i+j
            score+= float(cor[letters.index(w)][letters.index(word[k])])
    return score
def scoreWord(word):
    score = 0
    for i in range(5):
        w = word[i]
        score += float(probs[letters.index(w)][0])-float(probs[letters.index(w)][i+1])
        for j in range(4-i):
            k = i+j
            if letters[k] == w:
                score -= .5
    return score
def best10Guess(li):
    return bestNGuess(li,10)

def best10Correct(li):
    return bestNCorrect(li,10)

def bestNGuess(li,n):
    li.sort(reverse=True,key=scoreWord)
    return li[:n]
def bestNCorrect(li,n):
    li.sort(reverse=True,key= scoreCorrectWord)
    return li[:n]