list1 = [];
for i in range(0,9) :
    num = int(input());
    list1.append(num);

max = 0;
for i in range(0,9) :
    if max < list1[i] :
        max = list1[i];
seq = 0;
for i in range(0,9) :
    if max == list1[i] :
        seq = i+1;

print(max, seq);
