def main(wordlist):
       print(" ".join(sorted(list(set(wordlist)))))

if __name__ == '__main__':
    words = [w.strip(' ') for w in input("Enter words:").split(' ')]
    main(words)