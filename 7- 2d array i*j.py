def main():
    dimensions = inp.split(',')

    row = int(dimensions[0])
    col = int(dimensions[1])


    #simple way

    multilist = []
    for i in range(0, row):
        l = []
        for j in range(0, col):
            l.append(i*j)
        multilist.append(l)

    #comprehension way

    multilist = [[i*j for j in range(col)]  for i in range(row)]

    print(multilist)




if __name__=='__main__':
    inp = input("Enter x,y:")

    main()