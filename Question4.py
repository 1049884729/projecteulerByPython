'''

A palindromic number (回文数)reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数
Find the largest palindrome made from the product of two 3-digit numbers.
从两个3位数的乘积找到最大的回文数
'''

def palindromic(num):
    minNum=10**(num-1)
    maxNum=10**(num)#'''此处不减1,因为range的范围是<maxNum,不含有<='''
    palindSet=set()
    for digit in range(minNum,maxNum):
        for digit2 in range(minNum, digit):
            result=digit*digit2
            if(isPalindromic(result)):
                palindSet.add(result)
    maxPalindrome=max(palindSet)
    print(maxPalindrome)

def isPalindromic(result):
    '''if result is  A palindromic number,return True;else false '''
    temp=int(result)
    palindNum=0
    while(temp!=0):
            palindNum=palindNum*10+(temp%10)
            temp=int(temp/10)
    if(palindNum==result):
        return True
    else:
        return False

# print(isPalindromic(53))#测试是否是回文数
# palindromic(2)
palindromic(3)