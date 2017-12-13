'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import datetime
import math


def isPrime(numb):
    '''判断是否是素数'''
    if numb < 2: return False
    max = int(math.sqrt(numb)) + 1#如果是合数,肯定有个积的因数<这个数的平方根,一个大于这个数的平方根
    for n in range(2, max):
        if not numb % n and n != numb:
            return False  # 能整除,则不是素数
    return True


def belowPrime(maxPrime):
    '''指定最大的素数不能超过多少'''
    allPrime = set()
    prime = 0
    while (prime < maxPrime):
        if isPrime(prime) and prime != 1:
            allPrime.add(prime)
        if prime < 3:
            prime += 1
        else:
            prime += 2  # 奇数偶数筛选,偶数一定是合数,奇数可能是质数
    print("the sum of all the primes below two million is :%s" % sum(allPrime))


start = datetime.datetime.now()
belowPrime(2000000)
end = datetime.datetime.now() - start
print("spend time is :%ss" % end.seconds)
