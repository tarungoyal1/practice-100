# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.


def main(binlist):
    divisiblelist = [num for num in binlist if convertBinToInt(num)%5==0]
    if divisiblelist:print(", ".join(divisiblelist))
    else:print("No such number")

def convertBinToInt(binNum):
    i = 1
    integer = 0
    for digit in binNum[::-1]:
        if int(digit) == 1:
            integer += i
        i *= 2
    return integer




if __name__=='__main__':
    binarylist = [num.strip(' ') for num in input("Enter comma-seperated binary numbers:").split(',') if all((int(char) in [1, 0]) for char in num.strip(' '))==True]
    main(binarylist)