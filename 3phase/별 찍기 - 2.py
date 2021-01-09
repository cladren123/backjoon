#rjust(5) 5칸 자리수, 오른쪽 정렬

a = int(input());

for i in range(0,a) :
    for j in range(a,0,-1) :
        if i < j-1 :
            print(" ",end="");
        else :
            print("*",end="");
    print();