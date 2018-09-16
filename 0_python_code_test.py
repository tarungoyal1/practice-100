from itertools import islice, count
from math import sqrt

def fiboseries():
    a,b=0,1
    while 1:
        yield a
        a,b = b, a+b

def getPrimes():
    num=2
    if num==2:
        yield 2
        num=3
    while 1:
        flag=1
        for x in range(2, int(sqrt(num))+1):
            if num%x==0:
                flag=0
                break
        if flag==1:
            yield num
        num+=2

if __name__ == '__main__':
    # Dynamic Programming illustration
    # highly effecient code try with input value 10000 or more

    primecount = {}
    n = getPrimes()
    list = []

    for x in range(1, int(input("Enter the upper bound:")) + 1):
        list.append(next(n))
        primecount[x] = [x for x in list]

    for c, l in primecount.items():
        print(c, [x for x in l])

