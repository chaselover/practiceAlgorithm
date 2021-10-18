import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
a = list(map(int, input().split()))[::-1]
floor = [i for i in range(N, 1, -1)]
front = [1]
q = deque()
for command in a[1:]:
    if command == 1:
        q.appendleft(front.pop())
        front.append(floor.pop())
    elif command == 2:
        q.appendleft(floor.pop())
    else:
        q.append(floor.pop())
answer = front + list(q)
print(*answer)