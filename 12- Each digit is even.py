# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

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