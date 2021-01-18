
def pibo(num) :
    if num <= 1 :
        return num;
    return pibo(num-1) + pibo(num-2);

num = int(input());
print(pibo(num))