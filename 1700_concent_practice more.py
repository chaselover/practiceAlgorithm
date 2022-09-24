

N , K= map(int,input().split())
number = list(input())
number = list(map(int,number))

for _ in range(K):
    number.pop(number.index(min(number)))

number = list(map(str,number))
print(''.join(number))