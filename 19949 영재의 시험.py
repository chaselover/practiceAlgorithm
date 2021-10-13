import sys
input = sys.stdin.readline

ans = list(map(int, input().split()))
dp = [[[[-1 for score in range(11)] for pre2 in range(6)] for pre in range(6)] for depth in range(11)]

def make_dp(depth, pre, pre2, score):
    if dp[depth][pre][pre2][score] != -1:
        return dp[depth][pre][pre2][score]

    if depth == 10:
        return 1 if score >= 5 else 0

    cnt = 0
    for next_num in range(1, 6):
        if pre == pre2 and pre2 == next_num:
            continue
        if ans[depth] == next_num:
            cnt += make_dp(depth + 1, pre2, next_num, score + 1)
        else:
            cnt += make_dp(depth + 1, pre2, next_num, score)
    
    dp[depth][pre][pre2][score] = cnt
    return cnt

print(make_dp(0, 0, 0, 0))



# 풀이2
def solve(arr, depth, point):
    global ans
    if depth >= 6 and point <= depth - 6:
        return
    if depth == 10:
        if point >= 5:
            ans += 1
    else:
        for i in range(1, 6):
            ar = arr[:]
            ar.append(i)
            p = point + 1 if i == answers[depth] else point
            if depth >= 2:
                if not (i == ar[depth - 1] and i == ar[depth - 2]):
                    solve(ar, depth + 1, p)
            else:
                solve(ar, depth + 1, p)


answers = list(map(int, input().split()))
ans = 0
solve([], 0, 0)
print(ans)