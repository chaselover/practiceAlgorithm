import sys
input = sys.stdin.readline

def dfs(left, right, string):
    if len(string) == target:
        answers.add(string)
        return
    if left > 0:
        dfs(left - 1, right, string + N[left - 1:right + 1])
    if right < n:
        dfs(left, right + 1, string + N[left: right + 2])

N = input().rstrip()
n = len(N)
target = n * (n + 1) // 2
answers = set()
for i in range(n):
    dfs(i, i, N[i])
print(len(answers))




def dfs(string):
    global cnt
    if len(n) == 1:
        cnt +=1
        return
    L = set(list(string))
    if len(L) == 1:
        cnt +=1
        return
    dfs(string[1:])
    dfs(string[:-1])

n = input()
cnt = 0
dfs(n)
print(cnt)