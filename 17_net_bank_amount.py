# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def calculateNetBalance(translist):
    netbalance=0
    for type, amount in transactionlist:
        if type=='d':
            netbalance+=int(amount)
        elif type=='w':
            netbalance-=int(amount)
    return netbalance


if __name__=='__main__':

    # first ask for input as per the format
    transactionlist = []

    while 1:
        i = str(input())
        if i:
            if i[0].lower()=='d' or i[0].lower()=='w':
                if i[2:].isdigit():
                    transactionlist.append(tuple(i.split(' ')))
        else:
            break

    print('netbalance = ', calculateNetBalance(transactionlist))