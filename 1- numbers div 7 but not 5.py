nums = [x for x in range(2000, 3201) if x%7==0 and x%5!=0]
s = ','.join([str(x) for x in nums])
print(s)