'''
the url is https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

1^2 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and
 the square of the sum.

'''


def suqearesOfSum(maxNum):
    '''和的平方'''
    sumSuquares = 0
    for num in range(1, maxNum + 1):
        sumSuquares += num
    return sumSuquares ** 2


import math


def sumOffuqeares(maxNum):
    '''平方的和'''
    sumSuquares = 0
    for num in range(1, maxNum + 1):
        sumSuquares += math.pow(num, 2)
    return sumSuquares


def difference(maxNum):
    result = suqearesOfSum(maxNum) - sumOffuqeares(maxNum)
    print(int(result))


difference(100)
