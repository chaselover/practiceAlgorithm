import sys

# 입력부
n,s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 이분 분할
m = n//2
n = n - m

# first : 왼쪽 Subset
first = [0] * (1<<n)

# 비트마스킹을 이용하여 Subset의 합을 담는다
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k)) > 0:
            first[i] += a[k]
            
# second : 오른쪽 Subset
second = [0]*(1<<m)
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] += a[k+n]
            
# first 오름차순 정렬, second 내림차순 정렬
first.sort()
second.sort(reverse = True)

# n, m = first의 길이, second의 길이
n = (1<<n)
m = (1<<m)
i = 0
j = 0
ans = 0
while i < n and j < m:

    # 같은 경우
    if first[i] + second[j] == s:
        # i,j를 이동
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        # 예외 처리
        while i < n and first[i] == first[i-1]:
            c1 += 1
            i += 1
        while j < m and second[j] == second[j-1]:
            c2 += 1
            j += 1
        # 전체 순서쌍 반영
        ans += c1*c2
        
    # 큰 경우 i만 이동
    elif first[i] + second[j] < s:
        i += 1
        
    # 작은 경우 j만 이동
    else:
        j += 1
        
# s가 0인 경우 공집합의 경우를 빼줘야 하므로 1감소
if s == 0:
    ans -= 1
    
# 정답 출력
print(ans)