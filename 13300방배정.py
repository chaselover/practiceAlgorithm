import sys
input = sys.stdin.readline

N, K = map(int, input().split())
students = [[0,0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    students[Y-1][S] += 1
answer = 0
for grade in students:
    for sex in grade:
        answer += sex//K
        if sex%K:
            answer += 1
print(answer)