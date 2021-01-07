a = input('put 2 numbers : ');
a = a.split(' ')


print(int(a[0])+int(a[1]))

a, b = map(int, input('두 수를 입력 : ').split()) #map은 str은 int로 변환해준다.
print(a+b)

a, b = input('두 수를 입력 : ').split()

print(a,b)