import sys
input = sys.stdin.readline

# 처음 첫요소,합0으로 들어가서 sum요소에 자기value더해주고 자기를포함하는 재귀와 포함하지 않는 재귀로 나눠서 다음 idx진행.
# 부분집합은 결국 요소를 포함하느냐 안하느냐 0과1인데서 착안한 탐색.
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - s_[idx])
    dfs(idx + 1, sum)


n, s = map(int, input().split())
s_ = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)