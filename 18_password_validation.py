def validatePassword(password, exp):

    # first check the length
    if len(password)<6 or len(password)>12:
        return False

    pset = set(list(password))

    if pset.isdisjoint(set(exp[0])):
        return False
    elif pset.isdisjoint(set(exp[1])):
        return False
    elif pset.isdisjoint(set(exp[2])):
        return False
    elif pset.isdisjoint(set(exp[3])):
        return False

    # may work but ineffecient
    # flagsum = sum(1 for e in exp if set(list(password)).issubset(e)==True)
    #
    # if flagsum<=3:
    #     return False

    return True

if __name__=='__main__':

    passwords = [x.strip() for x in str(input()).split(',')]

    exp = []

    # exp+=[chr(c) for c in range(97, 123)]
    # exp+=[chr(c) for c in range(65, 91)]
    # exp+=[n for n in range(0, 10)]
    # exp+=['$', '#', '@']

    exp.append([chr(c) for c in range(97, 123)])
    exp.append([chr(c) for c in range(65, 91)])
    exp.append([str(n) for n in range(0, 10)])
    exp.append(['$', '#', '@'])

    # we have created the expression list (exp ) above, had we made it in validatePassword function
    # it would've been created each time the function called like it is below, here we are just passing
    # already made expression

    validpasswords = [pas for pas in passwords if validatePassword(pas, exp)]

    if len(validpasswords)>0:
        print(' '.join(validpasswords))
