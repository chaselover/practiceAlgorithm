import sys
input = sys.stdin.readline


def calculate():
    global result
    # 각 플레이어의 구간, 위치정보
    player = [[0, 0] for _ in range(5)]
    # 각 경우의 수에서 포인트의 합
    sum_points = 0
    # 1턴 부터 10턴까지 실행.
    for i in range(1, 11):
        turn = turns[i]
        section, pos = player[turn]
        if section == -1: 
            return
        else:
            pos += dice[i]
            # 0번 구역일때는 섹션이 옮겨지거나 도착하거나 이동하거나
            if section == 0:
                if 20 < pos: 
                    player[turn] = [-1, -1]
                elif pos == 5: 
                    player[turn] = [1, 0]
                elif pos == 10: 
                    player[turn] = [3, 0]
                elif pos == 15: 
                    player[turn] = [2, 0]
                else: 
                    player[turn] = [section, pos]
            # 1번 구역일 떄는 쭉 가서 8 이상 가면 도착.
            elif section == 1:
                if pos >= 8: 
                    player[turn] = [-1, -1]
                # 4 이상이면 section 3 직진구간에서 칸수를 하나 빼줌.(가로구간은 사이 3칸, 세로구간은 2칸이기 때문에)
                elif pos >= 4: 
                    player[turn] = [3, pos - 1]
                else: 
                    player[turn] = [section, pos]
            elif section == 2:
                if pos >= 8: 
                    player[turn] = [-1, -1]
                elif pos >= 4: 
                    player[turn] = [3, pos - 1]
                else: 
                    player[turn] = [section, pos]
            elif section == 3:
                if pos > 6: 
                    player[turn] = [-1, -1]
                else: 
                    player[turn] = [section, pos]
            # 이동된 칸이 이미 말이 있던 칸이면 올바르지 않은 경우이므로 연산중지. 아니면 point합산.
            nx, ny = player[turn]
            if nx != -1:
                for k in range(1, 5):
                    if turn == k: 
                        continue
                    a, b = player[k]
                    if a == -1: 
                        continue
                    if idx[a][b] == idx[nx][ny]: 
                        return
                sum_points += points[nx][ny]
    result = max(result, sum_points)

# 10턴 경우의 수의 조합을 turns에 저장
def dfs(depth):
    if depth == 10:
        calculate()
        return
    # 각 턴에 1 ~ 4 중 하나의 말이 움직임.
    for i in range(1, 5):
        turns[depth] = i
        dfs(depth + 1)


turns = [0 for _ in range(11)]
points = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
[10, 13, 16, 19], [30, 28, 27, 26], [20, 22, 24, 25, 30, 35, 40]]
idx = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
[5, 21, 22, 23], [15, 24, 25, 26], [10, 27, 28, 29, 30, 31, 20]]

dice = [0] + list(map(int, input().split()))
result = 0
dfs(0)

print(result)