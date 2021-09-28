import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for num in range(1, N + 1):
    if num < 100:
        answer += 1
    else:
        digits = list(map(int, str(num)))
        if digits[0] - digits[1] == digits[1] - digits[2]:
            answer += 1
print(answer)