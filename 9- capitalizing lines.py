# Question 9
# Level 2
#
# Questions
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


def main(rawlines):
    caplines = [line.upper() for line in rawlines]
    print(caplines)




if __name__=='__main__':
    rawlines = []
    while True:
        s = input()
        if s:
            rawlines.append(s)
        else:
            break
    main(rawlines)
