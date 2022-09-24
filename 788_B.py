import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    k, *c = input().split()
    c = set(c)
    pre, life = 0, 0
    for i in range(n - 1):
        if s[i] in c:
            if not pre:
                pre = i
            else:

