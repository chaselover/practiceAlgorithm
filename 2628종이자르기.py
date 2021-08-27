import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cut_row = [0,M]
cut_col = [0,N]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if not a:
        cut_row.append(b)
    else:
        cut_col.append(b)
cut_row.sort()
cut_col.sort()

len_row = []
len_col = []
for i in range(1,len(cut_row)):
    len_row.append(cut_row[i] - cut_row[i-1])
for i in range(1,len(cut_col)):
    len_col.append(cut_col[i] - cut_col[i-1])
if not len_row:
    len_row.append(M)
if not len_col:
    len_col.append(N)
max_s = 0
for row in len_row:
    for col in len_col:
        max_s = max(max_s,row*col)
print(max_s)