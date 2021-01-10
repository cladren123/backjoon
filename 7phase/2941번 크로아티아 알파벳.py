
nu = input()
count = 0;

for i in range(0,len(nu)) :
    count += 1;
    if nu[i] == 'c' :
        if nu[i+1] == '=' :
            count -= 1;
        elif nu[i+1] == '-' :
            count -= 1;
    if nu[i] == 'd' :
        if nu[i+1] == 'z':
            if nu[i+2] == '=' :
                count -= 1;
        elif nu[i+1] == '-' :
            count -= 1;
    if nu[i] == 'l' :
        if nu[i+1] == 'j' :
            count -= 1;
    if nu[i] == 'n' :
        if nu[i+1] == 'j' :
            count -= 1;
    if nu[i] == 's' :
        if nu[i+1] == '=' :
            count -= 1;
    if nu[i] == 'z' :
        if nu[i+1] == '=' :
            count -= 1;
print(count);

"""
다른 사람의 숏코딩. 크로아티아 문자를 배열에 넣었고, 그 배열을 비교하면서 교체하는 방향으로 알고리즘을 구성했다.
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='];
b = input()
for i in a :
    b = b.replace(i, 'a') 
print(len(b))

replace 함수 
replace(old, new, [count]) , 찾을값, 바꿀값, 바꿀횟수
"""
