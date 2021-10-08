import sys
input = sys.stdin.readline


def check_mid(x, y):
    tmp = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if tmp:
                if tmp[-1] <= filters[i][j]:
                    tmp.append(filters[i][j])
                else:
                    for k in range(len(tmp)):
                        if filters[i][j] < tmp[k]:
                            tmp.insert(k, filters[i][j])
                            break
            else:
                tmp.append(filters[i][j])
    if tmp[4] >= T:
        return True
    return False


R, C = map(int, input().split())
filters = [list(map(int, input().split())) for __ in range(R)]
T = int(input())

cnt = 0
for i in range(R - 2):
    for j in range(C - 2):
        if check_mid(i, j):
            cnt += 1
print(cnt)