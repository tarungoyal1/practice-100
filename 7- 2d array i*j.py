# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

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