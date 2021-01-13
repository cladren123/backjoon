
num = int(input());
for i in range(0,num) :
    h,w,n = map(int, input().split())


    count = 0;

    for i in range(1,w+1):
        for j in range(1,h+1) :
            sil = (j*100) + i;
            count += 1;
            if count == n :
                break;
        if count == n :
            break;
    print(sil);
