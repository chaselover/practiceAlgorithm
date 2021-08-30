import sys
input = sys.stdin.readline

N = int(input())
maps = input()
cnt = 1
for i in range(1,N):
    if maps[i]=='E':
        if maps[i-1]=='W':
            cnt +=1
print(cnt)