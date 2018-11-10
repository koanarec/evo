import random
def evo(x):
        if random.randint(0,10) == 1:
                return x + 1
        elif random.randint(0,10) == 1:
                return x - 1
        else:
                return x

def cre(a):
	return a[0] * a[1]+ a[2]

def check(a,b,c):
        if cre(a) <= cre(b) or cre(c):
                a = b
        elif cre(b) <= cre(a) or cre(c):
                b = c
        else:
                c = a

creone = [10,10,10]
cretwo = [10,10,10]
crethree = [10,10,10]


def go(x):
        for x in creone:
                x = evo(x)
                print (creone)
        for x in cretwo:
                x = evo(x)
                print (cretwo)
        for x in crethree:
                x = evo(x)
                print(crethree)


	

        
                        

                




