import sys
input = sys.stdin.readline

def DFS(start,depth,sum_cow):
    if depth==M:
        if isPrime(sum_cow):
            answer.add(sum_cow)
    for i in range(start,N):
        if not visited[i]:
            visited[i]=True
            DFS(i+1,depth+1,sum_cow+H[i])
            visited[i]=False
            
def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

N,M = map(int,input().split())
H = list(map(int,input().split()))
visited = [False]*N
answer = set()

DFS(0,0,0)

if answer:
    print(*sorted(list(answer)))
else:
    print(-1)
