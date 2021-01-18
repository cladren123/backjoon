num = int(input())

soin = 2;

while True :
    if num % soin == 0:
        num = num / soin
        print(soin);
    else :
        soin += 1;

    if num == 1:
        break;
