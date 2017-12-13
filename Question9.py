'''
a + b + c = 1000.
a2+b2=C2
求 abc的积
'''
const=1000
def main():
    a=1
    b=1
    c=1000-a-b
    while(not pTrigle(a,b,c)):
        b+=1
        a=abc(b)
        c = const - a - b
        if(c<0):
            break

    print("a:%s b:%s c:%s"%(a,b,c))
    print("result: %s"%(a*b*c))
def abc(b):
    '''根据公式求出a和 b的关系'''
    if (2 * const - 2 * b)==0 :
        return b
    a = int((const ** 2 - 2 * const * b) / (2 * const - 2 * b))
    return a

def pTrigle(a,b,c):
    '''判断是否符合勾股定理'''
    if a**2+b**2==c**2:
        return True
    return False
main()