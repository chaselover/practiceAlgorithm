import sys
input = sys.stdin.readline 

def find(x): 
    if x == arr[x]: 
        return x 
    arr[x] = find(arr[x]) 
    return arr[x] 

def union(x, y): 
    x = find(x) 
    y = find(y) 
    
    if x < y: 
        arr[y] = x 
    else: 
        arr[x] = y 

N, M = map(int, input().split()) 
arr = [i for i in range(N)] 
for i in range(M): 
    a, b = map(int, input().split()) 
    if find(a) == find(b): 
        print(i+1) 
        exit()
    union(a, b) 
print(0)

