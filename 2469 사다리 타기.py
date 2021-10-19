import sys
input = sys.stdin.readline

k, n = int(input()), int(input())
start = []
for i in range(k):
    start.append(chr(ord('A') + i))
last = list(input().rstrip())
ladder_game = [list(input().rstrip()) for _ in range(n)]
flag = 0
for row in range(n):
    if flag: break
    for col in range(k - 1):
        if ladder_game[row][col] == '-':
            start[col], start[col + 1] = start[col + 1], start[col]
        elif ladder_game[row][col] == '?':
            flag = 1
            break

flag = 0
for row in range(n - 1, -1, -1):
    if flag: break
    for col in range(k - 1):
        if ladder_game[row][col] == '-':
            last[col], last[col + 1] = last[col + 1], last[col]
        elif ladder_game[row][col] == '?':
            flag = 1
            break

answer = ''
for i in range(k - 1):
    if start[i] == last[i + 1] and start[i + 1] == last[i] and (i==0 or answer[-1] == '*'):
        start[i], start[i + 1] = start[i + 1], start[i]
        answer += '-'
    elif start[i] == last[i]:
        answer += '*'
if len(answer) != k - 1:
    answer = 'x' * (k-1)
print(answer)