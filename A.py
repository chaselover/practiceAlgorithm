import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = defaultdict(int)
    check = False
    for num in arr:
        if num not in dic:
            dic[num] += 1
        else:
            check = True

    if 0 in dic:
        print(n - dic[0])
    else:
        if check:
            print(n)
        else:
            print(n + 1)