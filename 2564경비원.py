import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
store = []
for _ in range(K):
    store_dir, dist = map(int, input().split())
    if store_dir==1:
        y = M
        x = dist
    elif store_dir==2:
        y=0
        x = dist
    elif store_dir==3:
        x=0
        y=M-dist
    else:
        x=N
        y = M-dist
    store.append([x,y])
dongguen_dir, dist = map(int, input().split())
if dongguen_dir==1:
    y = M
    x = dist
elif dongguen_dir==2:
    y=0
    x = dist
elif dongguen_dir==3:
    x=0
    y=M-dist
else:
    x=N
    y = M-dist
answer = 0
for store_x,store_y in store:
    if not abs(store_x-x) == N and not abs(store_y-y)==M:
        answer += abs(store_x-x) + abs(store_y-y)
    else:
        answer += min(x+y+store_x+store_y,2*N+2*M-(x+y+store_x+store_y))
print(answer)