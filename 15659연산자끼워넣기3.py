import sys
input = sys.stdin.readline

def dfs(expression, depth, use_cnt):
    global max_result, min_result
    if depth == N:
        tmp = eval(expression)
        max_result = max(max_result, tmp)
        min_result = min(min_result, tmp)
        return
    if use_cnt[0] < p_cnt:
        use_cnt[0] += 1
        dfs(expression + "+" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[0] -= 1
    if use_cnt[1] < mi_cnt:
        use_cnt[1] += 1
        dfs(expression + "-" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[1] -= 1
 
    if use_cnt[2] < mu_cnt:
        use_cnt[2] += 1
        dfs(expression + "*" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[2] -= 1
 
    if use_cnt[3] < d_cnt:
        use_cnt[3] += 1
        dfs(expression + "//" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[3] -= 1
 
 
N = int(input())
nums = list(map(int, input().split()))
p_cnt, mi_cnt, mu_cnt, d_cnt = map(int, input().split())
max_result, min_result = -float('inf'), float('inf')
dfs(str(nums[0]), 1, [0, 0, 0, 0])
print(max_result)
print(min_result)
