"""
N개의 회의
ST, FT 주어짐.
회의실 사용 최대로.
"""

N = int(input())
meetings = [[0]*2 for _ in range(N)]

for i in range(N):
    st, ft = map(int, input().split())
    meetings[i][0] = st
    meetings[i][1] = ft

minsort = sorted(meetings,key = lambda a:a[0])
minsort = sorted(meetings,key = lambda a:a[1])

minft = 0
cnt=0
for i,j in minsort:
    if i>=minft:
        cnt += 1
        minft = j

print(cnt)
