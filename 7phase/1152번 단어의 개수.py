
nu = input()

count = 0

if nu[0] == ' ' :
    for i in range(0,len(nu)-1) :
        if nu[i] == ' ':
            count += 1;
else :
    count += 1;
    for i in range(0, len(nu) - 1):
        if nu[i] == ' ':
            count += 1;
print(count);
