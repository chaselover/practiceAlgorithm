import sys
# 입력부
n,s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
# 이분 분할
m = n//2
n = n - m
# first : 왼쪽 Subset
# 왼쪽의 경우의 수.
first = [0] * (1<<n)
# 비트마스킹을 이용하여 Subset의 합을 담는다
# 왼쪽에서 n개를 고르는 1<<n의 경우의 수에대해 k번째 숫자를 골랐는지 확인하고 골랐으면 a[k]를 first에 더해 저장.(모든 고른 숫자를 찾아 그 값을 저장.)
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k)) > 0:
            first[i] += a[k]
# second : 오른쪽 Subset
# 오른쪽도 동일하게 진행.
second = [0]*(1<<m)
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] += a[k+n]
# first 오름차순 정렬, second 내림차순 정렬
first.sort()
second.sort(reverse = True)
# n, m = first의 길이, second의 길이
n,m,i,j,ans = (1<<n),(1<<m),0,0,0
while i < n and j < m:
    # 합이 s인경우.왼쪽의 어떤 경우와 오른쪽의 어떤경우의 합이 s인경우.
    if first[i] + second[j] == s:
        c1,c2 = 1,1
        i += 1
        j += 1
        # 예외 처리 (왼쪽에서 합이 같은 모든 인자에 대해 스킵.idx만와 카운트 증가시킴.)
        while i < n and first[i] == first[i-1]:
            c1 += 1
            i += 1
        while j < m and second[j] == second[j-1]:
            c2 += 1
            j += 1
        # 전체 순서쌍 반영(앞에서 first[i]라는 값을 갖는 경우의수*오른쪽에서 second(j)라는 값을 갖는 경우의수)
        ans += c1*c2
    # 합이 s보다 작은경우 오름차순 정렬인 i만 이동.
    elif first[i] + second[j] < s:
        i += 1
    # 합이 s보다 큰경우 내림차순 정렬인 j만 이동.
    else:
        j += 1
# s가 0인 경우 공집합의 경우를 빼줘야 하므로 1감소
if s == 0:
    ans -= 1
# 정답 출력
print(ans)