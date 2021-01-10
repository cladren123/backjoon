
nu = input();
nu = list(nu);

list1 = []

sum = 0;

for i in nu :
    if ord(i) >= 87 :
        list1.append(9);
        sum += 10;
    elif ord(i) >= 84 :
        list1.append(8);
        sum += 9;
    elif ord(i) >= 80 :
        list1.append(7);
        sum += 8;
    elif ord(i) >= 77 :
        list1.append(6);
        sum += 7;
    elif ord(i) >= 74 :
        list1.append(5);
        sum += 6;
    elif ord(i) >= 71 :
        list1.append(4);
        sum += 5;
    elif ord(i) >= 68 :
        list1.append(3);
        sum += 4;
    elif ord(i) >= 65 :
        list1.append(2);
        sum += 3;
print(sum);
