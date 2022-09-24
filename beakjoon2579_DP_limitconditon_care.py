import sys

n = int(sys.stdin.readline())

s = list(map(int,sys.stdin.readline().split()))

max = 0
sum = 0


for i in range(n):
    if sum>0:
        sum += s[i]
        if sum>max:
            max = sum
    else:
        sum = s[i]

print(max)