import collections, sys
input = sys.stdin.readline



N = int(input())
queue = collections.deque()

for order in range(N):
    p = list(input().split())
    if p[0] == 'push':
        queue.append(p[1])
    elif p[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif p[0] == 'size':
        print(len(queue))
    elif p[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif p[0] =='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif p[0] =='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

