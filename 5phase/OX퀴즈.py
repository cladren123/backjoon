num = int(input());

#view1 = input().split(); #list 뛰어쓰기를 구분으로 하나의 요소로서 들어간다.

for i in range(0,num) :
    view = input()  # str형식으로 들어간다.
    sum = 0;
    count = 0;
    for i in view :
        if i == 'O' :
            count += 1;
            sum += count;
        if i == 'X' :
            count = 0;
    print(sum);