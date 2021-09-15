import sys
input = sys.stdin.readline

N = int(input())
state, cnt = {}, 0
for _ in range(N):
    a, b = map(int, input().split())
    if a in state and state[a] != b: cnt += 1
    state[a] = b
print(cnt)