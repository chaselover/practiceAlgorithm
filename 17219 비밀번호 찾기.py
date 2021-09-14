import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    address, pw = input().split()
    dic[address] = pw
for _ in range(M):
    print(dic[input().rstrip()])