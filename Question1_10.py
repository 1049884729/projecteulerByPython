#解决projecteuler.net 网上的问题

#Question1:3或5的倍数，算出和
class ThreeOrFive(object):
    def __init__(self,maxnumber):
        self.maxnumber=maxnumber
    def calculte(self):
        '''解决Question 1的问题'''
        allSet=set()
        for number in range(0,self.maxnumber):
            if number%3==0  or number%5==0:
                allSet.add(number)
                print(number)
        sumresult=sum(allSet)
        print(sumresult)
example=ThreeOrFive(10)
example.calculte()
example=ThreeOrFive(1000)
example.calculte()