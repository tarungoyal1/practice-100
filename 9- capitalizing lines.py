
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
