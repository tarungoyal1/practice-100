def main(sentence):
    counts = calculate(sentence)
    for key,val in counts.items():
        print(key,val)


def calculate(sentence):
    return {"UPPER":sum(1 for x in list(sentence) if str(x).isupper()), "LOWER":sum(1 for x in list(sentence) if str(x).islower())}



if __name__== '__main__':
    main(input("Enter the sentence:"))