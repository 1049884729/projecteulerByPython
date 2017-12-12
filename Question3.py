'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


def prime(destNumber):
    remainder = 1
    while (destNumber > 1):
        if destNumber % remainder == 0:
            destNumber = destNumber / remainder
            if (remainder != 1):
                print(remainder)
        remainder += 1


# prime(13195)
prime(600851475143)
