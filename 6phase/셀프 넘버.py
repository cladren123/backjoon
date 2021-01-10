def selfnum (n) :
    s = n;
    min = n;
    while True :
        con = min % 10;
        min = min // 10;
        s += con;
        if min == 0 :
            break;
    return s;

list1 = []
for i in range(0,15000) :
    list1.append(0);

for i in range(0,10000) :
    list1[selfnum(i)] += 1;
for i in range(0,10000) :
    if list1[i] == 0 :
        print(i);

"""
next = 0
for value in list(str(n)) :
    next += int(value)

if count in excep:
    continue;
else :
    print(count)
다른 사람은 배열을 비교하는 것으로 알고리즘을 구성했다.

"""