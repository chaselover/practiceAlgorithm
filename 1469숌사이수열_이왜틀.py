import sys
input = sys.stdin.readline

def DFS(idx,answer):
    if idx==length:
        print(*answer)
        exit()
    for num in X:
        if not visited[num]:
            continue
        elif visited[num]==1:
            if idx>num and answer[idx-num-1]==num:
                visited[num]-=1
                DFS(idx+1,answer+[num])
                visited[num]+=1
        else:
            visited[num]-=1
            DFS(idx+1,answer+[num])
            visited[num]+=1

# 집합 X의 모든 수는 두번등장
# i등장하고 cnt해서 i+1후에는 i가 다시 나와야함.

N = int(input())
X = list(map(int,input().split()))
visited ={x:2 for x in X}
arr = X+X
length = len(arr)
arr.sort()

for num in X:
    visited[num]-=1
    DFS(1,[num])
    visited[num]+=1
print(-1)