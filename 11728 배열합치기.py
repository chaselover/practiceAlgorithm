import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
ai = 0
bi = 0
answer = []
while 1:
    if arr_a[ai] <= arr_b[bi]:
        answer.append(arr_a[ai])
        ai += 1
    else:
        answer.append(arr_b[bi])
        bi += 1
    if ai == N or bi == M:
        answer += arr_a[ai:] + arr_b[bi:]
        break
print(*answer)