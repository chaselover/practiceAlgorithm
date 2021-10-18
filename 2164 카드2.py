import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
while len(q) != 1:
    q.popleft()
    if len(q) == 1:
        break
    q.rotate(-1)

print(q.pop())