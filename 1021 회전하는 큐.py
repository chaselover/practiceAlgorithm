import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())    
position = list(map(int, input().split())) 
q = deque([i for i in range(1, n+1)])  

move = 0   
for num in position:
    if q.index(num) < len(q)/2: 
        while q[0] != num:  
            q.rotate(-1)
            move += 1
    else:   
        while q[0] != num:
            q.rotate(1)
            move += 1
    if q[0] == num:  
        q.popleft()
        continue
print(move)


# 다른풀이 / 안돌리고 연산후 삭제.
n, m = map(int, input().split())
dq = [i for i in range(1, n+1)]

ans = 0

for find in map(int, input().split()):
    ix = dq.index(find)
    ans += min(len(dq[ix:]), len(dq[:ix]))
    dq = dq[ix+1:] + dq[:ix]

print(ans)