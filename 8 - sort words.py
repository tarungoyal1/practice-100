def main(wordlist):
    wordlist.sort()
    print(','.join(wordlist))

if __name__ == '__main__':
    words = [w.strip(' ') for w in input("Enter words:").split(',')]
    main(words)