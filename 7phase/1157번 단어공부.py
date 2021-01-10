num = input()

num = num.upper();
num = list(num);


list1 = []
for i in range (0,26) :
    list1.append(0);

for i in num :
   list1[ord(i)-65] += 1;

max = 0;
for i in range(0,26) :
    if max < list1[i] :
        max = list1[i]
list2 = [];
for i in range(0,26) :
    if max == list1[i] :
        list2.append(i);

if len(list2) > 1:
    print('?');
else :
    print(chr(list2[0] + 65));




