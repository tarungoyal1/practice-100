def main(l, u):
    numbers = []
    for number in range(l, u+1):
        if all((int(digit) %2==0) for digit in str(number))==True:
            numbers.append(str(number))

    print(",".join(numbers))


if __name__ == '__main__':
    lower = int(input("Enter lower limit:"))
    upperlimit = int(input("Enter upper limit:"))
    main(lower, upperlimit)