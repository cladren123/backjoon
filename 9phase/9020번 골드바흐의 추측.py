
import sys;

def Primenum(n) :
    for i in range(2, int(n**0.5+1)) :
        if n % i == 0 :
            return False
    return True

p = []
for i in range(2, 10000):
    if Primenum(i):
        p.append(i)

for k in range(0, int(input())) :
    n = int(sys.stdin.readline())
    for i in range(n//2, 1, -1) :
        if i in p and n-i in p :
            a,b = i, n-i
            break
        else :
            pass
    print(a,b);


"""
con = int(input())
for i in range(0,con) :
    num = int(sys.stdin.readline())
    primelist = []
    for i in range(2, num):
        if Primenum(i):
            primelist.append(i)

    list1= [0,0]

    for i in range(0, len(primelist)) :
        for j in range(i, len(primelist)) :
            if num == primelist[i] + primelist[j] :
                list1[0] = primelist[i]
                list1[1] = primelist[j]
    print(list1[0],list1[1])
"""

