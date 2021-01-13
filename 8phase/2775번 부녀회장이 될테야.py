



num = int(input())

for i in range(0,num) :
    b = int(input());
    a = int(input());

    list1 = [];
    list2 = [];

    sum = 0;
    for i in range(0,a) :
        list1.append(i+1);
        list2.append(0);

    for i in range(0,b) :
        sum = 0;
        for j in range(0,len(list1)) :
            sum += list1[j]
            list2[j] = sum

        for c in range(0, len(list2)) :
            list1[c] = list2[c];

    print(list1[len(list1)-1])








































"""
t = int(input())

for _ in range(t):
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력

"""
