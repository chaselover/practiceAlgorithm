import sys
input = sys.stdin.readline
from math import ceil

N = int(input())
S = input().rstrip()
cnt = 0
for char in S:
    if char != "C":
        cnt += 1
answer = ceil((N - cnt) / (cnt + 1))
print(answer)