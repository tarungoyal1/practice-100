# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def main(wordlist):
       print(" ".join(sorted(list(set(wordlist)))))

if __name__ == '__main__':
    words = [w.strip(' ') for w in input("Enter words:").split(' ')]
    main(words)