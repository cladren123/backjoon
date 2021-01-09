
num = [];
for i in range(0,10) :
    a = int(input());
    num.append(a%42);
num = set(num);
print(len(num));



