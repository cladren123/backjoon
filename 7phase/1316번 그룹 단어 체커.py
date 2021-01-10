
result = 0
for i in range(int(input())) :
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

"""
find 함수 
찾을 값의 자릿수를 알려준다. 가장 먼저 있는 자릿값을 돌려준다.

result = 0
for i in range(int(input)) : 
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
"""