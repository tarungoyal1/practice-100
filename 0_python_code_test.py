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
        yield 3
        yield 5
        yield 7
    num=7
    while 1:
        num+=2
        if num%3==0:
            continue
        if num%5==0:
            continue
        if num%7==0:
            continue

        flag=1
        i=5
        w=2
        while i*i <= num:
            if num%i==0:
                flag=0
                break
            i+=w
            w=6-w
        if flag==1:
            yield num

if __name__ == '__main__':
    # Dynamic Programming illustration
    # AKS primality test algo used
    # highly effecient code try with input value 10000 or more

    primecount = {}
    n = getPrimes()
    list = []

    for x in range(1, int(input("Enter the upper bound:")) + 1):
        list.append(next(n))
        primecount[x] = [x for x in list]

    for c, l in primecount.items():
        print(c, [x for x in l])

