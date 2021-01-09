"""
count = 0;
while count<5 :
    count +=1;
    a,b = map(int, input().split());
    print(a+b);
"""

while True :
    try :
        A, B =map(int, input().split());
        print(A+B);
    except :
        break;
#에러가 발생하면 while문을 종료한다.


