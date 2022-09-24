import sys
input = sys.stdin.readline
from itertools import combinations


N,S = map(int,input().split())
super_set = list(map(int,input().split()))
cnt = 0

# 1개뽑는조합~n개뽑는조합까지 모든 부분집합에 대해 조사 가능. 
# 부분집합의 요소들의 합이s가 되는지만 조사하고 버림.
for i in range(1,N+1) :
    sub_set = list(combinations(super_set,i))
    for c in sub_set :
        if sum(c) == S :
            cnt +=1
            
print(cnt)


