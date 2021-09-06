import sys, collections
input = sys.stdin.readline
deque = collections.deque

# 핵심은 y의 높이에 따라 모든 set을 만들고 거기에 x를 넣어주었다는 것.
# 그럼 y +- 2 범위내에서 set들만 뒤져주면 쉬움.
n, m = map(int, input().split())
v = [set() for _ in range(200001)]
for i in range(n):
    x, y = map(int, input().split())
    v[y].add(x)

Q = deque([(0, 0, 0)]) #(x, y, dist)
while Q:
    x, y, d = Q.popleft()
    if y == m: 
        print(d)
        exit()
    for ny in range(y - 2, y + 3):
        if ny < 0 or ny > m: 
            continue
        for nx in range(x - 2, x + 3):
            if nx not in v[ny]: 
                continue
            v[ny].remove(nx)
            Q.append((nx, ny, d + 1))
print(-1)