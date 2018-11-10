import random
import math

def mute(a):  # this is the mutation engine which mutates the creatues.
  number = len(a)-1
  while number != -1:
    for x in a:
      if random.randint(0,1) ==  1:
        a[number] = a[number] + 1
      if random.randint(0,1) ==  0:
        a[number] = a[number] - 1
    number = number -1
    
def fitness(x):  # this is the objective function for the creatures.
  return (x[0]+x[1]+x[2])

def largeche(cre):  # bad evo example
  totals = []
  for a in cre:
    totals.append([fitness(a),a])
  totals.sort()
  return(totals)

def breed(cre,totals):
  a = len(cre)
  a = math.ceil(math.sqrt(a))-1
  b = random.randint(0,a)
  
  for x in cre:
    if totals[0][1] == x:
      x.clear()
  cre.sort()
  for x in cre:
    if x == []:
      z = len(cre[(len(cre)-1)])
      while z != 0:
        x.append(cre[len(cre)-b-1][(z-1)])
        z = z -1
  return(cre)
  
def gendeath(cre):
  for a in cre:
    mute(a)
  totals = largeche(cre)
  cre = breed(cre,totals)

def go(x):
  cre = [[10,10,10,10,10,10],[10,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10],[10,10,10,5,10,10]]
  while x != 0:
    gendeath(cre)
    print(cre)
    x = x -1

go(1000)


