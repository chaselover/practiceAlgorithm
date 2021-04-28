import sys
input = sys.stdin.readline
n = int(input())
for test in range(n):
    stack = list(input())
    cnt = 0
    stack.pop()
    while stack:
        inspect = stack.pop()
        if inspect == ')':
            cnt += 1
        else:
            cnt -= 1
        if cnt<0:
            break
    if cnt ==0:
        print("YES")
    else:
        print("NO")