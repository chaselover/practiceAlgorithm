import sys
input = sys.stdin.readline

N = int(input())
files = [input().rstrip() for _ in range(N)]

for i in range(N-1):
    for j in range(i,N):
        if files[i][::-1] == files[j]:
            print(len(files[i]), files[i][len(files[i])//2])
            exit()