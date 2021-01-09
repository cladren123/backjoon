a = int(input());
b = int(input());
c = int(input());

num = a*b*c;
num = str(num); # str도 list다.

count = [];
for i in range(0,10) :
    count.append(0);

for i in range(0,10) :
    for j in num :
        if str(i)== j :
            count[i] += 1;

for i in range(0,10) :
    print(count[i]);