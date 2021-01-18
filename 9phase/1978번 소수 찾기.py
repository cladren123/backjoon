
num = int(input())

numbers = input().split();

for i in range(0, len(numbers)) :
    numbers[i] = int(numbers[i])

count = 0
for i in numbers :
    count1 = 0
    for j in range(1,i+1) :
        if i % j == 0 :
            count1 += 1
    if count1 == 2 :
        count += 1;
print(count);





