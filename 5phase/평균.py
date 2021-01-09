a = int(input());
num = input().split();

for i in range(0,a) :
    num[i] = float(num[i]);
max = 0;
for i in range(0,a) :
    if max < num[i] :
        max = num[i];
sum=0;
for i in range(0,a) :
    sum += num[i] / max * 100;
print(sum/a);
