def main(sentence):
    counts = calculate(sentence)
    for key,val in counts.items():
        print(key,val)


def calculate(sentence):
    return {"LETTERS":sum(1 for x in list(sentence) if str(x).isalpha()), "DIGITS":sum(1 for x in list(sentence) if str(x).isnumeric())}



if __name__== '__main__':
    main(input("Enter the sentence:"))