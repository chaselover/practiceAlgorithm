import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
idx = 0
cnt = 0
dict_c = ['c=','c-','z=','d-','lj','nj','s=','z=']
while idx < n :
    if idx+2 < n and s[idx:idx+3]=='dz=':
        idx += 3
        cnt += 1
        continue
    if idx+1 < n:
        check = s[idx:idx+2]
        if check in dict_c:
            idx += 2
            cnt += 1
            continue
    idx += 1
    cnt += 1
print(cnt)