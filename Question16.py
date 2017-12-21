'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
'''

import math
#method one
def getSum(number):
    result=int(math.pow(2,number))
    sum=0
    print(result)
    divide=10
    while(result!=0):
        sum+=result%divide
        result=result//divide
    return sum
#method two
def getSumTwo(number):
    result=str(int(math.pow(2,number)))
    listSum=list()
    for i in result:
        listSum.append(int(i))
    return sum(listSum)
# result=getSum(1000)
result=getSumTwo(1000)
print(result)