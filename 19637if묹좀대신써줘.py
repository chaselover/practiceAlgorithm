import sys
input=sys.stdin.readline

from bisect import bisect_left

N,M = map(int,input().split())
names=[]
grades=[]
for _ in range(N):
    name,grade = input().split()
    names.append(name)
    grades.append(int(grade))

for _ in range(M):
    check=int(input())
    print(names[bisect_left(grades,check)])