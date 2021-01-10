a = input()
list1 = [];
for i in range(0,26) :
    list1.append(-1);

for i in range(0,len(a)) :
    if list1[ord(a[i]) - 97] == -1 :
        list1[ord(a[i]) - 97] = i;
    else :
        continue;

for i in range(0,26) :
    print(list1[i], end=" ");




