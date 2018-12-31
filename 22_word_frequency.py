def main ():
    wordlist = str(input("Enter the input line:")).split(' ')

    countdict = {}

    wordlist = sorted(wordlist)
    for word in wordlist:
        countdict[word] = wordlist.count(word)
    for word, freq in countdict.items():
        print(word,':', freq)


if __name__ == '__main__':
    main()