def fiboseries():
    a,b=0,1
    while 1:
        yield a
        a,b = b, a+b

def getPrimes():
    num=2
    if num==2:
        yield 2
        yield 3
        yield 5
        yield 7
    num=7
    while 1:
        num+=2
        if num%3==0:
            continue
        if num%5==0:
            continue
        if num%7==0:
            continue

        flag=1
        i=5
        w=2
        while i*i <= num:
            if num%i==0:
                flag=0
                break
            i+=w
            w=6-w
        if flag==1:
            yield num

class Student:

    def __init__(self, id, name, age, course, human):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

        # here human is object of type human
        self.human = human

    def setInterests(self, interestList):
        self.interests = interestList


    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getcourse(self):
        return self.course

    def getInterests(self):
        return self.interests

    def getStudDetails(self):
        alldetails = {}

        alldetails['id'] = self.getid()
        alldetails['name'] = self.getname()
        alldetails['age'] = self.getage()
        alldetails['course'] = self.getcourse()
        alldetails['interests'] = self.getInterests()

        for tkey, tvalue in self.human.getHumanDetails().items():
            alldetails[tkey] = tvalue

        return alldetails


class Human:

    def __init__(self, h, w, ec, sc, qrc):

        if not h.isdigit() or not w.isdigit():
            raise ValueError("Entered height {}  or weight {} is not numeric".format(h,w))
        if not ec.isalpha() or not sc.isalpha():
            raise ValueError("Entered eyecolor {} or skin color {} is not string".format(ec, sc))
        if not qrc[:2].isdigit() or not  qrc[2:].isalpha():
            raise ValueError("Entered qrcode for human is not valid".format(qrc))

        self._height = h
        self._weight = w
        self._eyecolor = ec
        self._skincolor = sc
        self._qrcode = qrc

    def getHeight(self):
        return self._height

    def getWeight(self):
        return self._weight


    def getEyecolor(self):
        return self._eyecolor

    def getSkincolor(self):
        return self._skincolor

    def getQRcode(self):
        return self._qrcode

    def getHumanDetails(self):
        return {
            'height': self.getHeight(),
            'weight': self.getWeight(),
            'eyecolor': self.getEyecolor(),
            'skincolor': self.getSkincolor(),
            'qrcode': self._qrcode
            }




if __name__ == '__main__':
    # Dynamic Programming illustration
    # AKS primality test algo used
    # highly effecient code try with input value 10000 or more

    # primecount = {}
    # n = getPrimes()
    # list = []
    #
    # for x in range(1, int(input("Enter the upper bound:")) + 1):
    #     list.append(next(n))
    #     primecount[x] = [x for x in list]
    #
    # for c, l in primecount.items():
    #     print(c, [x for x in l])

    ##########################################################


    h = Human(input("Enter height:"),input("Enter weight:"),input("Enter eyecolor:"),input("Enter skincolor:"),input("Enter qrcode:"))

    student  = Student(int(input("Enter id:")), str(input("Enter name:")), int(input("Enter age:")), str(input("Enter course:")), h)

    student.setInterests([i.strip() for i in str(input('Enter interests(, separated):')).split(',')])

    studentDetails = student.getStudDetails()


    for key, value in studentDetails.items():
        if key=='interests':
            print(key,':')
            for v in value:
                # v is an interest
                print(v)
        else:
            print(key,'=', value)
