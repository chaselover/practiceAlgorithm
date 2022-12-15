import sys
input = sys.stdin.readline

def sol(x):
    if visited[x]:
        return False
    
    visited[x] = 1
    
    for i in edge[x]:
        if not b[i] or sol(b[i]):
            b[i] = x
            a[x] = i
            
            return True
        
    return False


dx = [-1, 0, 1, 1, 0, -1]
dy = [1, 1, 1, -1, -1, -1]

c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    
    room = []
    for i in range(n):
        room.append(list(map(str, input().rstrip())))
        
    
    edge = [[] for i in range(n * m + 1)]
    a = [0] * (n * m + 1) # 홀수 열
    b = [0] * (n * m + 1) # 짝수 열
    
    empty = 0
    
    for q in range(m):
        for p in range(n):
            if room[p][q] == 'x':
                continue
                
            empty += 1
            
            if not q % 2:
                continue
                
            for i in range(6):
                np = p + dx[i]
                nq = q + dy[i]
                
                if np < 0 or np >= n or nq < 0 or nq >= m:
                    continue
                    
                if room[np][nq] == '.':
                    edge[p * m + q + 1].append(np * m + nq + 1)
                    
    
    count = 0
    for q in range(1, m, 2):
        for p in range(n):
            visited = [0] * (n * m + 1)
            if sol(p * m + q + 1):
                count += 1
                
    print(empty - count)