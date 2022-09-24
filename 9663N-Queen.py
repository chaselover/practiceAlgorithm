import sys
input = sys.stdin.readline

n = int(input())
check_row = [0 for _ in range(16)]
result = 0

# 진입한 cnt값의 check[cnt]값은 지금 검사하는 열의 번호. 
# 이 열에 check_row[i]즉 같은 열에 퀸이있거나 
# 열의 차이=행의차이 즉 대각선 상에 퀸이 있으면 false반환.
def isTrue(x):
    for i in range(1, x):
        if check_row[x] == check_row[i] or abs(check_row[x] - check_row[i]) == x - i:
            return False
    return True

def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        # 퀸을 행의 1번부터 n번칸까지 놔보며 놓을 수 있나 확인해본다. 놓을 수 있으면 cnt+1 다음행으로 진입.
        for i in range(1, n + 1):
            check_row[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)
dfs(1)
print(result)
