import random
cre1 = [1,1]
cre2 = [1,1]
cre3 = [1,1]

def mute(a):
    q = len(a)-1
    for x in a:
        while q != -1:
            if random.randint(0,8) ==  1:
                if a[q] <9:
                    a[q] = a[q] + 1
            if random.randint(0,8) ==  0:
                if a[q] > 1:
                    a[q] = a[q] - 1
            q = q -1
        
        
def fitness(x):
    return (x[1])

      
 
def gendeath():
  #print ("start")
    mute(cre1)
    mute(cre2)
    mute(cre3)

  #print (totals)
    total1 = fitness(cre1)
    total2 = fitness(cre2)
    total3 = fitness(cre3)
    totals = [total1 , total2 , total3]
    totals.sort()

    if totals[0] == total1:
        x = 1
        while x != -1:
            if random.randint(1,2) == 1:
                cre1[x] = cre2[x]
                x= x -1
            else:
                cre1[x] = cre3[x]
                x = x -1
    elif totals[0] == total2:
        x = 1
        while x != -1:
            if random.randint(1,2) == 1:
                cre2[x] = cre1[x]
                x = x -1
            else:
                cre2[x] = cre3[x]
                x = x -1
    else:
        x = 1
        while x != -1:
            if random.randint(1,2) == 1:
                cre3[x] = cre1[x]
                x = x -1
            else:
                cre3[x] = cre2[x]
                x = x -1
    #print(cre1,cre2,cre3)

def go(x):
    while x != 0:
        gendeath()
        x = x -1
