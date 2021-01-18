small = int(input())
big = int(input())

def sosu(num) :
    count = 0;
    for i in range(1,num+1) :
        if num % i == 0 :
            count += 1
    if count == 2 :
        return 1;
    else :
        return 0;


list1 = []
for i in range(small,big+1) :
    if sosu(i) == 1 :
        list1.append(i);

if len(list1) == 0 :
    print(-1)
else :
    sum = 0
    for i in list1 :
        sum += i;
    print(sum)
    print(list1[0])



