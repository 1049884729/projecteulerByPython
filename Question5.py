'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def smallest(maxNum):
    smallestNumber = 10
    while not isRemainder(smallestNumber, maxNum):
        smallestNumber += 10#maxNum的最小公约数是10
    print(smallestNumber)

def isRemainder(remainder, maxNum):
    for devid in range(1, maxNum + 1):
        if (remainder % devid != 0):
            return False
    return True

print("__start__")
smallest(20)
print("__End__")




