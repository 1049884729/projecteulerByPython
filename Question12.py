'''
Let us list the factors of the first seven triangle numbers:
1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

n * (n + 1) / 2;
求第一个拥有超过500个因子的三角数?
'''

import math
print(int(math.sqrt(15)))
def divisors(integer):
    '''
    算法理由：如果一个数，能够整除某个数的平方根，那么肯定有一个比它大的数也能够整除；
    所以只需检查interger的平方根以下的所有整数即可
    比如数15，平方根整数是3，，所以只需要算1,2,3能否被15整除即可，能，则存在另一个被整除的，所以+2
    :param integer:
    :return:
    '''
    count = 0
    divided = int(math.sqrt(integer))+1
    for i in range(1, divided):
        if integer % i is 0:
            count += 2
    return count


def getNumber(num):
    '''
    :param num: 因子数
    :return:
    '''
    count=0
    temp=1
    index=1
    while(count<num):
         temp=int((index**2+index)/2)
         count=divisors(temp)
         if(count<num):
             index+=1
    print(temp)

getNumber(500)

