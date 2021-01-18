import math

def isPrime(num) :
    n = int(math.sqrt(num))
    if num == 1:
        return False;
    for k in range(2, n+1) :
        if num % k == 0 :
            return False
    return True;

numlist = list(range(2,246912))
sortlist = []
for i in numlist :
    if isPrime(i) :
        sortlist.append(i)

while True :
    n = int(input())
    if n == 0 :
        break;
    count = 0;
    for i in sortlist :
        if n < i <= n*2:
            count += 1
    print(count)
