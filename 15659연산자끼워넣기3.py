import sys
input = sys.stdin.readline

def dfs(exp: str, idx: int, used: list):
    global n, a, add, sub, mul, div, maxV, minV
    if idx == n:
        maxV = max(maxV, eval(exp))
        minV = min(minV, eval(exp))
        return
    if used[0] < add:
        used[0] += 1
        dfs(exp + "+" + str(a[idx]), idx + 1, used)
        used[0] -= 1
    if used[1] < sub:
        used[1] += 1
        dfs(exp + "-" + str(a[idx]), idx + 1, used)
        used[1] -= 1
 
    if used[2] < mul:
        used[2] += 1
        dfs(exp + "*" + str(a[idx]), idx + 1, used)
        used[2] -= 1
 
    if used[3] < div:
        used[3] += 1
        dfs(exp + "//" + str(a[idx]), idx + 1, used)
        used[3] -= 1
 
 
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxV, minV = -float('inf'), float('inf')
dfs(str(a[0]), 1, [0, 0, 0, 0])
print(maxV)
print(minV)
