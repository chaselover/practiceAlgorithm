import sys
input = sys.stdin.readline


s = input().rstrip()
n = len(s)
for i in range(n):
    if s[i] == '_':
        pass