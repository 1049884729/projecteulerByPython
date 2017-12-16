'''
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
'''
def getChains(origin):
    index=1
    while(origin!=1):

        if  origin%2:
           #奇数
           origin=3*origin+1
        else:
            origin/=2
        index+=1
    return index
def getMax(maxNumber):
    maxDir={}
    index=1
    while(index<=maxNumber):
        v=getChains(index)
        maxDir[v]=index
        index+=1
    return list(maxDir.values())[list(maxDir.keys()).index(max(maxDir.keys()))]
print(getMax(1000000))