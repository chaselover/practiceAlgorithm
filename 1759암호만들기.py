import sys
input = sys.stdin.readline
from itertools import combinations

L,C = map(int,input().split())
secret = list(input().split())

# 암호는 사전순 sorted되어있다.
secret.sort()

# 최소한개모음 두개자음
mom_char = ['a','e','i','o','u']

combs = list(combinations(secret,L))
ans = []

for chars in combs:
    mom_cnt=0
    child_cnt=0
    for char in chars:
        if char in mom_char:
            mom_cnt+=1
        else:
            child_cnt +=1
    if mom_cnt>=1 and child_cnt>=2:
        ans.append(chars)


for chars in ans:
    print(''.join(chars))