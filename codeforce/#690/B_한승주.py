import sys
input = sys.stdin.readline


for test in range(int(input())):
    n = int(input())
    cnt = 0
    while n > 2019:
        n -= 2020
        cnt += 1
    print("YES" if n <= cnt else "NO")