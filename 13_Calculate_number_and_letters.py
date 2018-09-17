# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def main(sentence):
    counts = calculate(sentence)
    for key,val in counts.items():
        print(key,val)


def calculate(sentence):
    return {"LETTERS":sum(1 for x in list(sentence) if str(x).isalpha()), "DIGITS":sum(1 for x in list(sentence) if str(x).isnumeric())}



if __name__== '__main__':
    main(input("Enter the sentence:"))