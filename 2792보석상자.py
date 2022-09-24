import sys
input = sys.stdin.readline
from math import ceil

def answer():
    global n, m, jewerlies
    start, end, ans = (1, max(jewerlies), 0)

    while(start <= end):
        mid, sections = ((start+end)//2, 0)

        for i in jewerlies:
            sections += ceil(i/mid)
        # 보석을 나눈 분배가 아이들의 수보다 적으면  일단 ans에 저장.그리고 분배 섹션 늘리고 보석수 줄이기 위해 왼쪽으로 이동.
        if sections <= n: 
            ans, end = (mid, mid-1)
        else: 
            start = mid+1
    return ans

n, m = map(int, input().split())
jewerlies = []
for _ in range(m):
    jewerlies.append(int(input()))

print(answer())