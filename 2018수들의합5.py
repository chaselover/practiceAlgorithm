import sys
input = sys.stdin.readline

N = int(input())
prex_sum, left = 0, 0
answer = 0

# 슬라이딩 윈도우
for right in range(1,N+1):
    # 결론적으로 end는 기존 슬라이딩 윈도우 처럼 일정 간격이 고정이 아니라
    # 일정 합 이상이되면 알아서 그 간격이 줄어드는 시스템이므로 한번 순회로 전부 조사 가능.
    while left < N and prex_sum < N:
        prex_sum += left+1
        left += 1
    if prex_sum == N:
        answer += 1
    prex_sum -= right
print(answer)