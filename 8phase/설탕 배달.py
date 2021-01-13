num = int(input());
hill = num//5;
while True :
    lenga = num - hill * 5;
    if lenga % 3 != 0 :
        if hill == 0 :
            print(-1)
            break;
        hill -= 1
    elif lenga % 3 == 0 :
        hill += lenga/3
        print(int(hill))
        break;