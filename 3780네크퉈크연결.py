import sys
input = sys.stdin.readline

def find(x):
    if parent[x]==x:
        return x
    # 부모쪽 length모두 갱신
    tmp = find(parent[x])
    # 내 length 갱신
    length[x] += length[parent[x]]
    # 부모값 저장
    parent[x] = tmp
    # 반환.
    return tmp

def union(a,b):
    length[a] = abs(a-b) % 1000
    parent[a] = b

for test in range(1,int(input())+1):
    N = int(input())
    parent = {i:i for i in range(1,N+1)}
    length = {i:0 for i in range(1,N+1)}
    while True:
        command = input().split()
        if command[0]=='E':
            find(int(command[1]))
            print(length[int(command[1])])
        elif command[0]=='I':
            union(int(command[1]),int(command[2]))
        else:
            break