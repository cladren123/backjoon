a,b = input().split();

list1 = [];
list2 = [];

a = list(a)
b = list(b)

for i in range(0,len(a)) :
    list1.append(a.pop());
for i in range(0,len(b)) :
    list2.append(b.pop());

list1 = (''.join(list1)); #list를 string 으로 만들어준다.
list2 = (''.join(list2));

if int(list1) > int(list2) :
    print(list1);
else :
    print(list2);