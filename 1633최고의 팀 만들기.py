from operator import itemgetter

inputList = []

while True:
    try:
        line = input()
        inputList.append(list(map(int, line.split())))
    except EOFError:
        break

# id 값 추가
# 0 - id, 1 - while value, 2 - black value
for idx, val in enumerate(inputList):
    inputList[idx].insert(0, idx)

orderByWhite = sorted(inputList, key=itemgetter(1, 2), reverse=True)
orderByBlack = sorted(inputList, key=itemgetter(2, 1), reverse=True)
checkList = [-1] * len(inputList)

cnt = 0
whiteIndex = 0
blackIndex = 0
whiteCnt = 0
blackCnt = 0
result = 0

whiteSameCnt = 0
blackSameCnt = 0

while whiteCnt + blackCnt < 30:
    if checkList[orderByWhite[whiteIndex][0]] == 1:
        whiteIndex = whiteIndex + 1
        continue
    if checkList[orderByBlack[blackIndex][0]] == 1:
        blackIndex = blackIndex + 1
        continue

    if blackCnt >= 15:
        if whiteSameCnt > 0 and orderByWhite[whiteIndex][1] < orderByWhite[whiteIndex][2]:
            whiteSameCnt = whiteSameCnt - 1
            result = result + orderByWhite[whiteIndex][2]
        else:
            result = result + orderByWhite[whiteIndex][1]
        checkList[orderByWhite[whiteIndex][0]] = 1
        whiteIndex = whiteIndex + 1
        whiteCnt = whiteCnt + 1
        continue
    elif whiteCnt >= 15:
        if blackSameCnt > 0 and orderByBlack[blackIndex][2] < orderByBlack[blackIndex][1]:
            blackSameCnt = blackSameCnt - 1
            result = result + orderByBlack[blackIndex][1]
        else:
            result = result + orderByBlack[blackIndex][2]
        checkList[orderByBlack[blackIndex][0]] = 1
        blackIndex = blackIndex + 1
        blackCnt = blackCnt + 1
        continue

    if orderByWhite[whiteIndex][1] > orderByBlack[blackIndex][2]:
        checkList[orderByWhite[whiteIndex][0]] = 1
        result = result + orderByWhite[whiteIndex][1]
        whiteCnt = whiteCnt + 1
        whiteIndex = whiteIndex + 1
    elif orderByWhite[whiteIndex][1] < orderByBlack[blackIndex][2]:
        checkList[orderByBlack[blackIndex][0]] = 1
        result = result + orderByBlack[blackIndex][2]
        blackCnt = blackCnt + 1
        blackIndex = blackIndex + 1
    else:
        # orderdByWhite 내 black 값과 orderedByBlack 내 white 값을 비교해 작은값이 있는 것을 우선순위로 넣어줌
        # 이후 메인 값 비교시 낮은 값이 들어가는 상황을 막기 위함
        if orderByWhite[whiteIndex][2] > orderByBlack[blackIndex][1]:
            checkList[orderByBlack[blackIndex][0]] = 1
            result = result + orderByBlack[blackIndex][2]
            blackCnt = blackCnt + 1
            blackIndex = blackIndex + 1
            blackSameCnt = blackSameCnt + 1
        elif orderByWhite[whiteIndex][2] < orderByBlack[blackIndex][1]:
            checkList[orderByWhite[whiteIndex][0]] = 1
            result = result + orderByWhite[whiteIndex][1]
            whiteCnt = whiteCnt + 1
            whiteIndex = whiteIndex + 1
            whiteSameCnt = whiteSameCnt + 1
        else:
            if whiteCnt < blackCnt:
                checkList[orderByWhite[whiteIndex][0]] = 1
                result = result + orderByWhite[whiteIndex][1]
                whiteCnt = whiteCnt + 1
                whiteIndex = whiteIndex + 1
                whiteSameCnt = whiteSameCnt + 1
            else:
                checkList[orderByBlack[blackIndex][0]] = 1
                result = result + orderByBlack[blackIndex][2]
                blackCnt = blackCnt + 1
                blackIndex = blackIndex + 1
                blackSameCnt = blackSameCnt + 1

print(result)


# 풀이2:
"""BOJ Q1633 - 최고의 팀 만들기 (https://www.acmicpc.net/problem/1633)

DP of O(|candidates| * |white player| * |black player|)
"""

import sys

BLACK_PLAYER_COUNT = 15
WHITE_PLAYER_COUNT = 15

player_scores = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]
table = [[0 for x in range(BLACK_PLAYER_COUNT + 1)] for y in range(WHITE_PLAYER_COUNT + 1)]
next_table = [[0 for x in range(BLACK_PLAYER_COUNT + 1)] for y in range(WHITE_PLAYER_COUNT + 1)]

# 백을 취할때랑 흑을취할때랑 취하지 않을떄중 큰 것을 고름.
for white_score, black_score in player_scores:
    for i in range(BLACK_PLAYER_COUNT + 1):
        for j in range(WHITE_PLAYER_COUNT + 1):
            next_table[i][j] = max(table[i][j],
                                   table[i - 1][j] + white_score if i > 0 else 0,
                                   table[i][j - 1] + black_score if j > 0 else 0)
    next_table, table = table, next_table
print(table[BLACK_PLAYER_COUNT][WHITE_PLAYER_COUNT])




#dp
li = []
while True:
    try:
        temp = list(map(int, input().split()))
        li.append(temp)
    except:
        break

dp = [[0] * 16 for _ in range(16)] # dp[w][b]
for white, black in li:
    for w in range(15, -1, -1):
        for b in range(15, -1, -1):
            if w - 1 < 0 and b - 1 < 0:
                continue
            elif w - 1 < 0:
                dp[w][b] = max(dp[w][b - 1] + black, dp[w][b])
            elif b - 1 < 0 :
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b])
            else:
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b - 1] + black, dp[w][b])       
            
print(dp[15][15])