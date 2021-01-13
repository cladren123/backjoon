import math
a, b, v = map(int, input().split());
count = math.ceil((v-a)/(a-b))
print(count+1);