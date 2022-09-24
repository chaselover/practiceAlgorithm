"""
N개의 회의
ST, FT 주어짐.
회의실 사용 최대로.
"""

N = int(input())
meetings = [[0]*2 for _ in range(N)]

for i in range(N):
    st, ft = map(int, input().split())
    meetings[i][1] = st
    meetings[i][0] = ft

minsort = sorted(meetings)
minft = minsort[0][0]
cnt=1
for i in range(N):
    if minft <= minsort[i][1]:
        cnt+=1
        minft = minsort[i][0]

print(minsort)
