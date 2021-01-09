import sys

a = int(sys.stdin.readline());

for i in range(0,a) :
    b = list(map(int, sys.stdin.readline().split()));
    print(int(b[0]) + int(b[1]));