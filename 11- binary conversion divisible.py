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