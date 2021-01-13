"""
1 +6
7 +12
19 +18
20~37
"""

num = int(input())
count = 1;
while num > 1 :
    num -= 6*count
    count += 1
print(count)