import sys
input = sys.stdin.readline


N, L = map(int, input().split())
h_arr = list(map(int, input().split()))
h_arr.sort()
for h in h_arr:
    if L >= h:
        L += 1
        continue
    break
print(L)