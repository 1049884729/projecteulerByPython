'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
What is the 10 001st prime number?
'''
# print(bool(0) is False)

def isPrime(numb):
    '''判断是否是素数'''
    for n in range(2,numb+1):
        if not numb%n and n!=numb:
            return False#能整除,则不是素数
    return True
def indexPrime(index):
    '''指定 index位的素'''
    prime=1
    tempIndex=1
    while(tempIndex<=index):
        prime += 1
        if isPrime(prime):
            tempIndex+=1
    print(prime)
indexPrime(6)

