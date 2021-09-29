import sys
input = sys.stdin.readline

A, B = input().split()
# 그냥 B에 A매칭시키면서 차이 가장 작은거 찾아서 출력.
min_cnt = float('inf')
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if B[i+j] != A[j]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)