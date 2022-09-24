# 순열

def permute(arr): 
    result = [arr[:]] 
    c = [0] * len(arr) 
    i = 0 
    while i < len(arr):
        if c[i] < i: 
            if i % 2 == 0: 
                arr[0], arr[i] = arr[i], arr[0] 
            else: 
                arr[c[i]], arr[i] = arr[i], arr[c[i]] 
                
            result.append(arr[:]) 
            c[i] += 1
            i = 0 
        else: 
            c[i] = 0 
            i += 1 
            return result

# 재귀순열
def perm(lis, n): 
    result = [] 
    if n > len(lis): 
        return result 
    if n == 1: 
        for li in lis: 
            result.append([li]) 
    elif n > 1: 
        for i in range(len(lis)): 
            tmp = [i for i in lis] 
            tmp.remove(lis[i]) 
        for j in perm(tmp, n-1): 
                result.append([lis[i]]+j) 
    return result 

n = int(input()) 
lis = list(i for i in range(1, n+1)) 
for li in perm(lis,n): 
    print(' '.join(list(map(str, li))))

# 리스트 그래프
s = [[0]*6 for i in range(6)] s[1][2] = 1 s[2][1] = 1 s[1][3] = 1 s[3][1] = 1 s[2][4] = 1 s[4][2] = 1 s[2][5] = 1 s[5][2] = 1

# dic그래프
adj_list = {1: set([2,3]), 2: set([1,4,5]), 3: set([1]), 4: set([2]), 5: set([2])}

# bfs

def bfs(graph, start): 
    visited = [] 
    queue = [start]
    while queue: 
        n = queue.pop(0) 
        if n not in visited: 
            visited.append(n) 
            queue += graph[n] - set(visited) 
    return visited

# deque bfs

from collections import deque 

def bfs_dequeue(graph, start): 
    visited = [] 
    queue = deque([start])
    
    while queue: 
        n = queue.popleft() 
        if n not in visited: 
            visited.append(n) 
            queue += graph[n] - set(visited)
    return visited
