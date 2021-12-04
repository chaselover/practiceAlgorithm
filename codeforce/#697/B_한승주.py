import sys
input = sys.stdin.readline


for test in range(int(input())):
    n = int(input())
    s = input().rstrip()
    answer = '2020'
    if s[0] + s[-3:] == answer or s[:2] + s[-2:] == answer or s[:3] + s[-1] == answer or s[:4] == answer or s[-4:] == answer:
        print("YES")
    else:
        print("NO")