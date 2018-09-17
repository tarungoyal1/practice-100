# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def main(value):
    print(calculate(value))


def calculate(value):
    indval = []
    for i in range(1, 5):
        indval.append(int(str(value)*i))
    return sum(indval)




if __name__=='__main__':
    main(int(input("Enter value of a:")))