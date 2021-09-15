import sys
input = sys.stdin.readline

N = int(input())
state = {}
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a not in state:
        state[a] = b
        continue
    if state[a] != b:
        cnt += 1
print(cnt)