import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
i=666
while cnt <=10000:
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
    i+=1