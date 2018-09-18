class Divisible:

    def divisible_by_7(self, n):
        num=0
        while num<=n:
            if num%7==0:
                yield num
            num+=1


def main():
    d = Divisible();
    nums =[str(n) for n in d.divisible_by_7(int(input("Enter n:")))]
    print(','.join(nums))

if __name__ == '__main__':
    main()