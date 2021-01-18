
import math

def isPrime(num) :
    if num == 1:
        return False;
    n = int(math.sqrt(num))
    for k in range(2, n+1) :
        if num % k == 0 :
            return False
    return True;

m, n = map(int, input().split())
for k in range(m, n+1) :
    if isPrime(k) :
        print(k)




"""
시간초과됬음...
small,big = map(int, input().split())

for i in range(small,big+1) :
    count = 0
    for j in range(1, i+1) :
        if i % j == 0 :
            count += 1
    if count == 2 :
        print(i)
"""


