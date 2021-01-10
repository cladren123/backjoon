
num1 = int(input());

for ax in range(0, num1) :
    num2 = input().split();

    count = int(num2[0]);
    lit = num2[1];

    for i in range(0,len(lit)) :
        for j in range(0,count) :
            print(lit[i], end ='');
    print();
