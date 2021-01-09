
num = int(input());
for i in range(num) :
    stu = input().split();
    sum = 0;

    for i in range(0,len(stu)):
        stu[i] = int(stu[i]);

    for i in range(1,stu[0]+1) :
        sum += stu[i];

    ave = sum/(len(stu)-1)
    count = 0;

    for i in range(1,stu[0]+1) :
        if stu[i] > ave :
            count += 1
    print('%0.3f%%' % (count/(len(stu)-1) * 100));


