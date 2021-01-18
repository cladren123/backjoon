while True :
    a = input().split()

    if a == ['0','0','0'] :
        break;

    a = list(a)

    for i in range(0, len(a)) :
        a[i] = int(a[i]);

    max = 0
    for i in range(0, len(a)) :
        if max < a[i] :
            max = a[i];

    a.remove(max)

    if max * max == a[0] * a[0] + a[1] * a[1] :
        print('right');
    else :
        print('wrong');