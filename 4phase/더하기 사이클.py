n = int(input());
count = 0;
if n < 10:
    n = n * 10;
a=n;
while True :
    b = a%10 + a//10
    if b > 9 :
        b = b%10;
    a = ((a%10) * 10) + b
    count += 1;
    if n == a :
        break;

print(count);
