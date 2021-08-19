import sys
input = sys.stdin.readline

def DFS(sum_num, check):
    global cnt
    if sum_num > n:
        return
    if n == sum_num:
        cnt += 1
        if cnt == k:
            print(check[:-1])
            exit()
    for i in (1, 2, 3):
        DFS(sum_num + i, check+str(i)+'+')

cnt = 0
n, k = map(int, input().split())
DFS(0, '')
print(-1)