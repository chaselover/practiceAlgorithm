import sys
input = sys.stdin.readline

def check(li):
    sw = [False for _ in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue
        if abs(li[i] - li[i + 1]) > 1:
            return False
        # 내리막길
        if li[i] > li[i + 1]:
            # 내리막길 층수
            temp = li[i + 1]
            # 내리막길 앞쪽 l까지 체크.
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    # 층수 변동있으면 실패
                    if li[j] != temp: return False
                    # 이미 전 층수변동시 사용한 칸이면 실패
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
        # 오르막길
        else:
            temp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
    # 검사 끝나면 성공.
    return True

n, l = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

# 가로검사
cnt = 0
for i in s:
    if check(i):
        cnt += 1

# 세로배열 검사
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(s[j][i])
    if check(temp):
        cnt += 1

print(cnt)