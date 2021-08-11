import sys
input = sys.stdin.readline


# 검사하기
def is_matching(x, y, sticker, R, C):
    for i in range(x, x+R):
        for j in range(y, y+C):
            if notebook[i][j] and sticker[i-x][j-y]:
                return False
    for i in range(x, x+R):
        for j in range(y, y+C):
            if sticker[i-x][j-y]:
                notebook[i][j]=1
    return True


# 검사 시작지점 찾기. 
def find_sticker_start(sticker, R, C):
    for i in range(N-R+1):
        for j in range(M-C+1):
            if is_matching(i, j, sticker, R, C):
                return True
    return False


def turn_sticker(sticker):
    sticker = [k[::-1] for k in zip(*sticker)]
    return sticker


N, M, K = map(int, input().split())
notebook = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    # 스티커를 노트북에 붙일수 있는가 검사.
    for _ in range(4):
        if find_sticker_start(sticker, R, C):
            break # 가능? 붙히고 회전 종료.
        else: # 불가능? 90도 회전
            sticker = turn_sticker(sticker)
            R, C = C, R

# 모든 스티커 부착이 끝나면 칸수 세어보기.
sum_sticker = 0
for i in range(N):
    sum_sticker += sum(notebook[i])
print(sum_sticker)

