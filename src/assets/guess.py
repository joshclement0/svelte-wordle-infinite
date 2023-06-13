import pandas as pd
import numpy as np
from tqdm import tqdm
import json


df = pd.read_csv('all.csv')
allWordList = df.names.tolist()
df2 = pd.read_csv('sm.csv')
smWordList = df2.names.tolist()
df3 = pd.read_csv('history.csv')
usedWordList = df3["Wordle Answer"].tolist()
withoutHistory = [ w for w in smWordList if w not in usedWordList ]

def colorRow(answer,guess):
    colors = ['b' for i in range(5)]
    # // loop through guess and mark green if fully correct
    for i in range(5):
        if guess[i] == answer[i]:
            colors[i] = "g"
            # // remove letter from answer, so it's not scored again
            answer = answer.replace(guess[i], " ", 1)
        
    # // loop through guess and mark yellow if partially correct
    for i in range(5):
        if colors[i] != "g" and guess[i] in answer:
            colors[i] = "y"
            # // remove letter from answer, so it's not scored again
            answer = answer.replace(guess[i], " ", 1)
  
    return colors

def guessFull(guesses,easy=False):
    li = allWordList
    if easy:
        li = withoutHistory
    blackletters= ''
    for g in guesses:
        guess = g[0]
        resp = g[1]
        if resp == 'ggggg':
          return []
        for a,b,i in zip(guess,resp,range(5)):
            if b=='g':
                li = list(filter(lambda x: x[i]==a,li))
            if b=='y':
                li = list(filter(lambda x: a in x and x[i] != a, li))
            if b=='b' and guess.count(a)==1 and a not in blackletters:
                li = list(filter(lambda x: a not in x, li))
                blackletters+=a
    if len(li) ==0:
      print("no words found with those clues")
    return li
'''
testNextGuess([['raise','ybbyy'],['marsh','bbyyb'],['harsh','bbyyb'],['shorn','gbyyb'],['short','gbyyb'],['badly','ybbbb'],['kappa','bbbbb']])
'''    
def testNextGuess(guesses,hardmode=False,easyWords=False,verbose=True):
    if len(guesses) == 1:
      try:
        string = guesses[0][0]+guesses[0][1]
        with open(string+'.json') as svfile:
          scores = json.load(svfile)
          if hardmode:
            full = guessFull(guesses,easyWords)
            scores = {i[0]:i[1] for i in scores.items() if i[0] in full}
          elif easyWords:
            scores = {i[0]:i[1] for i in scores.items() if i[0] in smWordList}
            full = list(scores.keys())
          else:
            full = list(scores.keys())
          if verbose:
            full.sort(key=lambda x: scores[x])
            print(full[0],' - ',scores[full[0]])
          return scores
      except: 
        pass
    li = guessFull(guesses,True)
    if len(li) ==0:
      return {}
    if hardmode:
        full = guessFull(guesses,easyWords)
    elif easyWords:
        full = smWordList
    else:
        full = allWordList
    scores = {}
    for guess in tqdm(full):
      ans = []
      for a in li:
        ans.append(len(guessFull([*guesses,[guess,colorRow(a,guess)]], True)))
      scores[guess] = np.mean(ans)
    full.sort(key=lambda x: scores[x])
    if scores[full[0]]<2 and verbose:
      guesslist = guessFull(guesses,True)
      print("GUESS",guesslist)
    if verbose:
      print(full[0],' - ',scores[full[0]])
    if len(guesses) == 1:
        string = guesses[0][0]+guesses[0][1]
        with open(string+'.json','w') as svfile:
          json.dump(scores,svfile)
    return scores
'''
testQuordleNext([['raise',['ygyyy','ybbyy']]])
'''  
def testQuordleNext(guesses,hardmode=False):
    score = {}
    for t in range(len(guesses[0][1])):
        newguesses = [[g[0],g[1][t]] for g in guesses]
        newscore = testNextGuess(newguesses, hardmode, verbose=False)
        if len(newscore) ==0:
          print(" word already found")
        else:
          newfull = list(newscore.keys())
          newfull.sort(key=lambda x: newscore[x])
          print(" * ",newfull[0],' - ',newscore[newfull[0]])
          for key in newscore:
              if key in score:
                  score[key]+= newscore[key]
              else:
                  score[key] = newscore[key]
    full = list(score.keys())
    full.sort(key=lambda x: score[x])
    print(full[0],' - ',score[full[0]])
    return full[0],score

def FullGuess(guesses):
    a=testNextGuess(guesses,hardmode=False,easyWords=False,verbose=False)
    d=testNextGuess(guesses,hardmode=False,easyWords=True,verbose=False)
    b=testNextGuess(guesses,hardmode=True,easyWords=False,verbose=False)
    c=testNextGuess(guesses,hardmode=True,easyWords=True,verbose=False)
    for newscore in [a,d,b,c]:
        newfull = list(newscore.keys())
        newfull.sort(key=lambda x: newscore[x])
        print(" * ",newfull[0],' - ',newscore[newfull[0]])
    return a,b,c

def testGuess(easy=False):
    li = allWordList
    if easy:
      li = smWordList
    smli = [ w for w in smWordList if w not in usedWordList ]
    with open('rest2.csv','w') as f:
        f.write(",{},{},{}\n".format("max","average","median"))
        for guess in tqdm(li):
            ans = []
            for a in smli:
                ans.append(len(guessFull([[guess,colorRow(a,guess)]],easy)))
            f.write("{},{},{},{}\n".format(guess,max(ans),np.mean(ans),np.median(ans)))

if __name__ =="__main__":
    testGuess(True)

