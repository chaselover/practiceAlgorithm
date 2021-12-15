import sys
input = sys.stdin.readline

for test in range(int(input())):
    arr = list(map(int, input().split()))
    answer = []
    for i in range(2, 4):
        answer.append(arr[-1] - arr[-i])
    answer.append(arr[-1] - sum(answer))
    print(*answer)