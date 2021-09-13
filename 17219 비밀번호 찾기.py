import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    adress, pw = input().split()
    dic[adress] = pw
for _ in range(M):
    print(dic[input().rstrip()])