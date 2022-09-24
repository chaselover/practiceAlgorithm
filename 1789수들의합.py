import sys
input = sys.stdin.readline

N = int(input())
cnt=0
sum_num=0
i=1

while N >= sum_num:
    sum_num += i
    cnt += 1
    i += 1
print(cnt-1)