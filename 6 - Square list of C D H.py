import math

def main(list):
    c, h=50, 30
    qlist = []
    for item in list:
        q =  int(round(math.sqrt((2 * c * item)/h)))
        qlist.append(q)
    print(qlist)


if __name__=='__main__':
    l = [int(x) for x in input("Enter list of numbers:").split(',')]
    main(l)
